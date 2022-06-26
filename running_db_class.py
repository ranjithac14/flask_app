from db_class import DatabasehelperView
from login_flask_clasful import create_app

app = create_app()
DatabasehelperView.register(app)
if __name__ == '__main__':
  app.run(debug=True)