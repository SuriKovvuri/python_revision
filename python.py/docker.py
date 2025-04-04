'''
Docker:
   Docker is a open-source platform that allows you to Create, deploy and run in lightweight, portable containers.


1. What is a Docker Image?
Docker Images : A Docker image is like a blueprint or template for creating containers. It includes:
The application code
Runtime (e.g., Python, Node.js)
Libraries/dependencies
Configuration files

Important:
Blueprint/template for containers
Created using a Dockerfile
Stored in Docker Hub or private registries

You build an image once, and then you can run multiple containers from that image.


Think of it like:
Image = Class
Container = Object (instance)


🔍 Learn:
docker images
docker build
docker tag
docker push / docker pull


====docker images====
This command lists all images available locally on your machine.

Example output:

REPOSITORY   TAG         IMAGE ID       CREATED         SIZE
iotium/qa    clusterv1   c11024b22aee   23 months ago   1.88GB
REPOSITORY: Name of the image (e.g., iotium/qa)

TAG: Label or version (e.g., latest, v1, clusterv1)
IMAGE ID: Unique ID for the image
CREATED: When the image was built
SIZE: Disk size





2. What is Docker Containers?

Running instances of images
Isolated environment
Fast, lightweight

🔍 Learn:
docker run
docker ps / docker ps -a
docker start / stop / restart
docker exec (to run commands inside)
docker logs


3. Volumes?
Volume : Persistent data storage for containers

docker volume create
docker run -v


4. Docker Compose?
Define and run multi-container apps
Use a docker-compose.yml file

🔍 Learn:
docker-compose up / down
Services, volumes, networks in YAML



=======docker ps=======
This shows a list of currently running containers.
If nothing is running, it will return empty.

=======docker ps -a======
This shows all containers, including:

Running
Exited
Failed
Created but not started

Columns include:
CONTAINER ID: Unique ID of the container
IMAGE: Which image it's based on
COMMAND: Entry command used
STATUS: Running, Exited, etc.
NAMES: Auto-generated or user-assigned name

Summary
Command	What it shows
docker images	   All locally stored Docker images
docker ps	       Only running containers
docker ps -a	   All containers (running, exited, etc.)



Example of image convert to container

💡 Simple Explanation:
Step 1: You create a Docker Image
Imagine you're preparing a meal kit:

You pack all ingredients (code + libraries)

You add instructions (Dockerfile)

You seal the box → This is your image.

But it's not cooking yet — it's just ready.

Step 2: You run the image
Now you open the meal kit, follow the recipe, and start cooking.

This act of starting the meal = running a container.
'''


'''
🧰 Docker Features
Lightweight Containers :Uses system resources efficiently
                        No need to boot up a full OS like a VM

Portability:
"Works on my machine" becomes "Works everywhere"
Same image can run on Windows, Linux, Mac, cloud...

Isolation
Each container runs in its own isolated environment

Version Control for Images
You can tag versions of your image (like v1, latest)

Fast Startup
Containers start in seconds (much faster than VMs)

Docker Hub & Registries
Central place to share and pull images

Docker Compose
Manage multi-container apps (e.g., app + DB)

CI/CD Friendly
Easily integrates with Jenkins, GitHub Actions, etc.

Volume Management
Store persistent data outside containers

Networking Between Containers
You can link services (app ↔ database) easily

✅ Docker Advantages
Advantage	Why it’s Good
🚀 Speed	Containers start fast, use less memory
📦 Consistency	Same environment across dev, test, prod
🧪 Testing Friendly	Easily test in isolated environments
🔄 Rollback Easy	Use image versions to revert or redeploy quickly
💼 Scalable	Works well with orchestration (e.g., Kubernetes)
💻 Platform Independent	Run anywhere Docker is supported
🤝 Easy Collaboration	Share your Dockerfile or image with team via Docker Hub
⚠️ Docker Disadvantages
Disadvantage	Why it’s a Problem
🛠️ Not a full VM	Doesn’t replace all use cases of full virtual machines
💾 Data Persistence	If not managed well, data may be lost when container stops
🧑‍🔧 Learning Curve	Some learning needed if you're new to containers and image concepts
🐞 Debugging Issues	Debugging inside containers can be tricky sometimes
🖥️ GUI-based Apps	Running GUI apps in Docker is possible but not straightforward
🔐 Security Concerns	If not isolated properly, containers may pose security risks
📚 Heavy Images Possible	If not optimized, images can become large and slow to ship
👀 Summary:
What	Summary
Features	Portability, isolation, speed
Advantages	Fast, scalable, consistent
Disadvantages	Learning curve, persistence, security concerns
'''


'''
3. Dockerfile
A text file with instructions to build an image

Example:

Dockerfile
FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

🔍 Learn:
How to write Dockerfiles
Common instructions (FROM, COPY, RUN, CMD, etc.)
'''


'''
2. What is the difference between a Docker image and a container?
Docker Image	                              Docker Container
Blueprint or snapshot	                      Running instance of the image
Read-only	                                  Read-write (creates a new layer)
Built once, used many times	                  Can be started/stopped multiple times
Created using Dockerfile	                  Created using docker run


3. How do you create a Docker image?
docker build -t <image-name> .
docker build -t myapp .

'''