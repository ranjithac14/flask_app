from login_class import LoginView
from login_flask_clasful import create_app

app = create_app()
LoginView.register(app)
if __name__ == '__main__':
  app.run(debug=True)
