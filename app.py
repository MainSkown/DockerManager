import os

import docker.errors
from flask import Flask, jsonify
from dotenv import load_dotenv
from flask import request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import asyncio

from Service.authentication import login, logout
from Middleware.middleware import authentication_middleware
from Repository.repo import create_new_container, get_all_info, get_status, turn_on, turn_off
from Repository.repo import AlreadyRunning, AlreadyDead

# Initiating app
app = Flask(__name__)
load_dotenv()

app.secret_key = os.getenv('SECRET_TOKEN')

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=['200 per day', '50 per hour'],
    storage_uri="memory://"
)


@app.route('/login', methods=['POST'])
@limiter.limit('3/day')
def LOGIN():
    response = login(request.get_json()['password'])
    if not response:
        return {'message': 'NOT ALLOWED'}, 401
    else:
        return response


@app.route('/logout', methods=['POST'])
def LOG_OUT():
    logout(request.cookies.get('session_id'))
    return {'message': 'OK'}, 200


## Create new container
# url:string -> github link to repo
# optional:
# system: string
@app.route('/container/create', methods=['POST'])
@authentication_middleware
def POST_CREATE_CONTAINER():
    result = create_new_container(request.get_json()['url'], request.get_json()['name'])
    if not result[0]:
        return {'message': result[1]}, 500
    else:
        return {'message': 'Created container successfully'}, 201


## Check status
@app.route('/container/status/<string:container_id>', methods=['GET'])
@authentication_middleware
def GET_STATUS(container_id):
    try:
        return {'status': get_status(container_id)}, 200
    except docker.errors.NotFound:
        return {'message': 'Not found'}, 404


## Get all container info
@app.route('/container/all', methods=['GET'])
@authentication_middleware
def GET_ALL():
    containerStrings = get_all_info()
    if len(containerStrings) == 0:
        return {'message': 'There are no containers'}, 200
    else:
        return jsonify(containerStrings), 200


## Turn container on
@app.route('/container/on/<string:container_id>', methods=['POST'])
@authentication_middleware
def POST_TURN_ON(container_id):
    try:
        result = turn_on(container_id)
        if result:
            return {'message': 'Successfully started container'}, 201
        else:
            return {'message': 'Could not start container'}, 500
    except AlreadyRunning:
        return {'message': 'Container is already running'}, 409
    except docker.errors.NotFound:
        return {'message': 'Container not found'}, 404


## Turn off
@app.route('/container/off/<string:container_id>', methods=['POST'])
@authentication_middleware
def POST_TURN_OFF(container_id):
    try:
        result = turn_off(container_id)
        if result:
            return {'message': 'Successfully stopped container'}, 201
        else:
            return {'message': 'Could not stop container'}, 500
    except AlreadyDead:
        return {'message': 'Container is already dead'}, 409
    except docker.errors.NotFound:
        return {'message': 'Container not found'}, 404



if __name__ == '__main__':
    app.run()
