from functools import wraps
from flask import request, session


def authentication_middleware(func):
    @wraps(func)
    def _authenticate_middleware(*args, **kwargs):
        session_id = request.cookies.get('session_id')
        try:
            if session[session_id] is None:
                return {'message': 'NOT ALLOWED'}, 401
            else:
                return func(*args, **kwargs)
        except Exception as exc:
            print('Exception happened', exc)
            return {'message': 'Internal Server Error'}, 500

    return _authenticate_middleware
