docker stop login_container

docker stop login_authenticate_container

docker stop db_container

docker stop app_container

docker rm login_container

docker rm login_authenticate_container

docker rm db_container

docker rm app_container

docker image rm login_image

docker image rm login_authenticate_image

docker image rm db_image

docker image rm app_image
