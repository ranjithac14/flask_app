from functools import wraps

import jwt
import requests
from flask import request, session

from constants import HOST_NAME_IP
from db_helper import DBHelperView
from login_flask_clasful import create_app

app=create_app()
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        print(request.headers)
        if 'token' in session:
            token=session['token']
        # if 'x-access-token' in request.headers:
        #     token = request.headers['x-access-token']
        # if not token:
        #     return 'Unauthorized Access token!', 401
        if not token:
            return 'Unauthorized Access token!'
        data = jwt.decode(token, app.SECRET_KEY,algorithms="HS256")
        response_url = requests.get(
            'http://'+HOST_NAME_IP+':5003/databasehelper/check_user_found/' + data['user_id'])
        response_text = response_url.json()
        user_db = response_text["data"]["result_dict"]
        if not user_db:
            return 'no user found Unauthorized Access!', 401

        return f(*args, **kwargs)
    return  decorated