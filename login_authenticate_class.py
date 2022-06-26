from flask import render_template, request, flash,redirect,url_for,session
from flask_classful import FlaskView, route

from constants import HOST_NAME_IP
from db_class import DatabasehelperView
import mysql.connector
import regex as re
import jwt
import requests
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

from login_flask_clasful import create_app

app=create_app()
dbhelper = DatabasehelperView()
class LoginauthView(FlaskView):
    @route('/register_new_user', methods=['POST'])
    def register_new_user(self):
        user_name = request.form["email"]
        pass_word = request.form["pwd"]
        # user_db = requests.get('http://'+HOST_NAME_IP+':5003/databasehelper/check_user_found/'+user_name)
        # user_db=user_db.json()
        # user_db=user_db["data"]["result_dict"]
        # if user_db:
        #     return redirect('http://'+HOST_NAME_IP+':5000/login/login_page')
        # else:
        #     print(user_name)
        #     pass_word = generate_password_hash(pass_word)
        #     print(pass_word)
        #     inserted_txt = requests.get('http://'+HOST_NAME_IP+':5003/databasehelper/put_db/'+user_name+'/'+pass_word)
        #     inserted_txt = inserted_txt.text
        #     print(inserted_txt)
        #     if inserted_txt == "inserted":
        #         return redirect('http://'+HOST_NAME_IP+':5000/login/login_page')
        #     else:
        return redirect('http://'+HOST_NAME_IP+':5000/login/login_page')

    @route('/login', methods=['POST'])
    def post(self):
        # response = {
        #     "success": False,
        #     "message": "Invalid parameters",
        #     "token": ""
        # }
        # print("logging in")
        # auth = request.form
        # session['user'] = auth.get('Uname')
        # if not auth or not auth.get('Uname') or not auth.get('Pass'):
        #     response["message"] = 'Invalid data'
        #     return response, 422
        response_url = requests.get('/databasehelper/check_user_found/ranc1')
        response_text = response_url.json()
        print("login_autheticate_class : ",response_text)
        return "True"
        # user_db=response_text["data"]["result_dict"]
        # if not user_db:
        #     response["message"] = "Unauthorized Access!"
        #     return response, 401
        # if check_password_hash(user_db['password'], auth['Pass']):
        #     token = jwt.encode({
        #         'user_id': user_db['name'],
        #         'exp': datetime.utcnow() + timedelta(hours=1)
        #     }, app.SECRET_KEY)
        #     session["token"] = token
        return redirect('http://'+HOST_NAME_IP+':5001/application/app_page')