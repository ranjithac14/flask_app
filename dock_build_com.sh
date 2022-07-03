docker build -t login_image:v1 --target login-env .

docker build -t login_authenticate_image:v1 --target login-authenticate-env .

docker build -t db_image:v1 --target db-env .

docker build -t app_image:v1 --target app-env .

#docker run -d  -p 5000:5000 --net flask_app_network --name login_container --add-host="app-backend:172.27.48.1"  login_image

#docker run -d  -p 5002:5000 --net flask_app_network --name login_authenticate_container --add-host="app-backend:172.27.48.1"  login_authenticate_image

#docker run -d  -p 5003:5000 --net flask_app_network --name db_container --add-host="app-backend:172.27.48.1"  db_image

#docker run -d  -p 5001:5000 --net flask_app_network --name app_container --add-host="app-backend:172.27.48.1"  app_image
