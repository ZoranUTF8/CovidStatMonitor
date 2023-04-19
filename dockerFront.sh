# Change directory to the frontend folder
cd frontend/

# This command builds a Docker image with the tag frontend from the current directory (.). The image will be named frontend.
docker build -t frontend .

# This command creates a Docker network with the name my_network. A network is a virtual environment in which Docker containers can communicate with each other
# docker network create my_network   

# This command runs a Docker container with the name dockerize-frontend using the image frontend. The container will run in interactive mode (-it), expose port 8080 (-p 8080:8080) and connect to the my_network network. The --rm flag specifies that the container should be removed when it is stopped.
# docker run -it -p 8080:8080 --rm --network my_network  --name dockerize-frontend frontend
docker run -it -p 8080:8080 --rm --name dockerize-frontend frontend

