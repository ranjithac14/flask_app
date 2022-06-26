from login_authenticate_class import LoginauthView
from login_flask_clasful import create_app

app = create_app()
LoginauthView.register(app)
if __name__ == '__main__':
  app.run(debug=True)