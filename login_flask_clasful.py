from flask import Flask

# we'll make a list to hold some quotes for our app
def create_app():
    app = Flask(__name__)
    app.SECRET_KEY='abc'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.config['SECRET_KEY']='abc'
    #app.config['MYSQL_HOST'] = 'localhost'
    #app.config['MYSQL_USER'] = 'root'
    #app.config['MYSQL_PASSWORD'] = ''
    #app.config['MYSQL_DB'] = 'user_info'
    #app.config['MYSQL_PORT'] = '3306'

    return app
