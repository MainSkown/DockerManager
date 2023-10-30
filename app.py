import os

from flask import Flask, request, make_response
from dotenv import load_dotenv
from Service.authentication import login, logout
from flask import request

# Initiating app
app = Flask(__name__)
load_dotenv()

app.secret_key = os.getenv('SECRET_TOKEN')


@app.route('/login', methods=['POST'])
def LOGIN():
    response = login(request.get_json()['password'])
    if not response:
        return {'message': 'NOT ALLOWED'}, 401
    else:
        return response, 202


@app.route('/logout', methods=['POST'])
def LOG_OUT():
    logout(request.cookies.get('session_id'))
    return {'message': 'OK'}, 200


## Create new container
# url:string -> github link to repo
# optional:
# system: string
@app.route('/container/create', methods=['POST'])
def POST_CREATE_CONTAINER():
    return {'message': 'NOT IMPLEMENTED'}, 501


## Check status
# id -> container id
@app.route('/container/status/<string:id>', methods=['GET'])
def GET_STATUS(id):
    return {'message': 'NOT IMPLEMENTED'}, 501


## Get all container info
@app.route('/container/all', methods=['GET'])
def GET_ALL():
    return {'message': 'NOT IMPLEMENTED'}, 501


## Turn container on
@app.route('/container/on/<string:id>', methods=['POST'])
def POST_TURN_ON(id):
    return {'message': 'NOT IMPLEMENTED'}, 501


## Turn off
@app.route('/container/off/<string:id>', methods=['POST'])
def POST_TURN_OFF(id):
    return {'message': 'NOT IMPLEMENTED'}, 501


## Change "always on" status
@app.route('/container/always_on/<string:id>', methods=['POST'])
def POST_ALWAYS_ON(id):
    return {'message': 'NOT IMPLEMENTED'}, 501


if __name__ == '__main__':
    app.run()
