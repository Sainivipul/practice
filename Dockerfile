#INSTALL - LINUX OS 
sudo apt install docker.io
sudo usermod -aG docker $USER
#DOCKER_IMAGE:
A Docker image is a lightweight, standalone, and executable package that includes everything needed to run a piece of software,
including the code, runtime, libraries, environment variables, and configurations.
Docker image create using docker file 
#DOCKER_CONTAINER:
Docker conmtainer is simmiler to docker image but docker image is blue print of docker container ,Docker container is the running instance created from that image
makes it easy to deploy transpor tnad manage application 

Docker file :
#Use an official runtime as a parent image :
    FROM python:3.8-slim-buster
# Set the working directory
    WORKDIR /app 
# Copy the current directory contents into the container at /app
    COPY ./app
# Install any needed packages specified in requirements.txt
    RUN pip install requirements.txt
# Make port available 
    EXPOSE 800
# Run any command at the time of conatiner start 
    CMD ["python", "app.py"]

#WORKFLOW : DOCKER FILE ---> DOCKER IMAGE --> DOCKER CONTAINER 
#DOCKER FILE >> IMAGE 
docker build -t {image-name} .
#DOCKER IMAGE TO CONTAINER 
docker run -p 4000:80 -d --name {container-name} --netowrk {network-name} {image-name}
#Basic commands-
docker --version             - check version 
docker image                 - list all images 
docker info                  - getdetailed infor about docker installation
docker pull [image-name]     - pull image from docker hub 
docker rmi [image-named]     - remove image 
docker ps                    - list running containers 
docker ps -a                 - list all containers (include stopped one )
docker start [container-name/id] - start a container 
docker stop [container-name/id]  - stop a container 
docker run [image-name]      - run new container 
docker run --name [custom-name] [image-name]  - run new container with custom name 
docker run -d [image-name]   - run container in detached mode 
docker run --rm [image-name] - run a container and remove after it exits
docker run -p hostport:container-port [image-name]  - run a container with mapped port 
docker rm [container-name/id]  - remove a container 
#DOCKER NETWORK COMMANDS 
docker network ls      - list docker networks
docker network create {network-name} -create a docker network 
docker network connect [netwok-name] [container-id/name]  -connect a container with network 
docker network disconnect [netwok-name] [container-name/id] -diconnect a network 
#docker volume commands 
docker volume ls       - list all volumes
docvker volume create [volume-name]  -create volume 
docker volume rm [volume name]       - remove a volume 
#docker inpection commands
docker inspect [container-name/id]   - inspect a container 
docker inspect [image-named]         - inspect image 
docker logs   [container-name/id]    - docker container logs 
#docker compose :
DOCKER COMPOSE FILE :|

Docker Compose is a tool for defining and managing multi-container Do
version: '3.8'

services:
  web:
    build: ./app
    ports:
      - "4000:80"
    volumes:
      - ./app:/code
    depends_on:
      - redis

  redis:
    image: "redis:alpine"
    ports:
      - "6379:6379"cker applications.
docker-compose ps     - view running containers
docker-compose build  - re build the image 
docker-compose up     - start services defined in "docker-compose.yml"
docker-compose up -d  - start service in deatcched mode
docker-compose down   - stop services 
