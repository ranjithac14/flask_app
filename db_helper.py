import mysql.connector
from flask import render_template
from flask_classful import FlaskView, route
from constants import (MY_SQL_DB_HOST,MY_SQL_USERNAME,MY_SQL_PASSWORD,MY_SQL_DB)


database=mysql.connector.connect(host=MY_SQL_DB_HOST, user=MY_SQL_USERNAME, passwd=MY_SQL_PASSWORD, database=MY_SQL_DB)
cursor=database.cursor()
class DBHelperView(FlaskView):
    @staticmethod
    def check_user_found(user_name):
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
        return result_dict

    @route('/login_page')
    def login_page(self):
        return render_template('loginpage.html')

    def put(self,user_name,password):
        query = "INSERT INTO login_info(id,name,password) VALUES(UUID(),%s,%s)"
        data = (user_name, password,)
        print(query)
        cursor.execute(query, data)
        database.commit()
        return True

    def get_users(self):
        cursor=database.cursor()
        query=("select name,password from login_info")
        cursor.execute(query)
        result=cursor.fetchall()
        result_dict={}
        for value in result:
            result_dict[value[0]]=value[1]
        return result_dict

    def update_user(self,user_name,user_password):
        query=("update  login_info set password = %s where name = %s")
        data=(user_name,user_password)
        result=cursor.execute(query,data)
        database.commit()
        return "updated"
