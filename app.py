import os

from flask import Flask
from dotenv import load_dotenv
from flask import request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from Service.authentication import login, logout
from Middleware.middleware import authentication_middleware

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
    return {'message': 'NOT IMPLEMENTED'}, 501


## Check status
# id -> container id
@app.route('/container/status/<string:id>', methods=['GET'])
@authentication_middleware
def GET_STATUS(id):
    return {'message': 'NOT IMPLEMENTED'}, 501


## Get all container info
@app.route('/container/all', methods=['GET'])
@authentication_middleware
def GET_ALL():
    return {'message': 'NOT IMPLEMENTED'}, 501


## Turn container on
@app.route('/container/on/<string:id>', methods=['POST'])
@authentication_middleware
def POST_TURN_ON(id):
    return {'message': 'NOT IMPLEMENTED'}, 501


## Turn off
@app.route('/container/off/<string:id>', methods=['POST'])
@authentication_middleware
def POST_TURN_OFF(id):
    return {'message': 'NOT IMPLEMENTED'}, 501


## Change "always on" status
@app.route('/container/always_on/<string:id>', methods=['POST'])
@authentication_middleware
def POST_ALWAYS_ON(id):
    return {'message': 'NOT IMPLEMENTED'}, 501


if __name__ == '__main__':
    app.run()
