
# This command changes the current working directory to the backend folder.
cd backend/
y
# This command builds a Docker image with the tag backend from the current directory (.). The image will be named backend.
docker build . -t backend

# This command runs a Docker container with the name backend using the image backend. The container will connect to the my_network network, expose port 8000 (-p 8000:8000), and run in the foreground. The --rm flag specifies that the container should be removed when it is stopped.
# docker run --name backend --rm --network my_network  -p 8000:8000 backend
docker run --name backend --rm -p 8000:8000 backend
