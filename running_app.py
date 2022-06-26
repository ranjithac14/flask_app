from application_class import ApplicationView
from login_flask_clasful import create_app


app = create_app()
ApplicationView.register(app)

if __name__ == '__main__':
  app.run(debug=True)