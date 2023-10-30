from flask import make_response, session
import os
from typing import Final
import uuid

# Constant to make sure it won't be changed
ADMIN_PASSWORD: Final[str] = os.getenv('PASSWORD')


def login(password: str):
    print(password)
    resp = make_response()
    if password == ADMIN_PASSWORD:
        session_id = str(uuid.uuid4())
        resp.set_cookie('session_id', session_id)
        session['ADMIN'] = session_id
        return resp
    else:
        return False


def logout(session_id:str):
    session.pop(session_id, None)
