import mysql.connector
from flask import render_template, request, Response, jsonify, json
from flask_classful import FlaskView, route
from constants import (MY_SQL_DB_HOST,MY_SQL_USERNAME,MY_SQL_PASSWORD,MY_SQL_DB)

database=mysql.connector.connect(host=MY_SQL_DB_HOST, user=MY_SQL_USERNAME, passwd=MY_SQL_PASSWORD, database=MY_SQL_DB, port='3306')
cursor=database.cursor()

class DatabasehelperView(FlaskView):
    @route('/check_user_found/<string:name>',methods=['GET'])
    def check_user_found(self,name: str):
        print("hi")
        user_name=name
        query = "select * from login_info where name = %s"
        data = (user_name,)
        cursor.execute(query, data)
        result = cursor.fetchone()
        result_dict = {}
        print(result)
        if result is not None:
            result_dict['id'] = result[0]
            result_dict['name'] = result[1]
            result_dict['password'] = result[2]
        return Response(
                response=json.dumps({
                    "data": {
                        "result_dict":result_dict
                    }
                }),
                status=201,
                mimetype="application/json"
            )

    @route('/put_db/<string:user_name>/<string:password>',methods=['GET'])
    def put_db(self, user_name : str, password : str):
        query = "INSERT INTO login_info(id,name,password) VALUES(UUID(),%s,%s)"
        data = (user_name, password,)
        print("db",user_name)
        print("db",password)
        cursor.execute(query, data)
        database.commit()
        return "inserted"

    def get_users(self):
        cursor = database.cursor()
        query = ("select name,password from login_info")
        cursor.execute(query)
        result = cursor.fetchall()
        result_dict = {}
        for value in result:
            result_dict[value[0]] = value[1]
        return result_dict

    def update_user(self, user_name, user_password):
        query = ("update  login_info set password = %s where name = %s")
        data = (user_name, user_password)
        result = cursor.execute(query, data)
        database.commit()
        return "updated"

