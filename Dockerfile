FROM python:3.11-slim
#Every Docker container starts from a base image. We're saying "start with a minimal Linux machine that already has Python 3.11 
#installed". The slim version is smaller and faster — it strips out things we don't need.

WORKDIR /app
#Inside the container, create a folder called /app and work from there. 
#All following commands run from this folder. Like doing cd /app.

COPY requirements.txt .
#copy requirements.txt to the current WORKDIR which is /app

RUN pip install -r requirements.txt
#Installs all your packages inside the container. We do this before copying the rest of code because of Docker's layer caching.

COPY . .
#Now copies ALL your project files (code, model, notebooks, etc.) into the container.

EXPOSE 8000
#Documents that this container uses port 8000. Think of it like labeling a door.

CMD ["uvicorn","src.main:app","--host","0.0.0.0","--port","8000"]
#The command that runs when the container starts. We're running uvicorn, 
#telling it to listen on 0.0.0.0 (all network interfaces, not just localhost) on port 8000. 
#The 0.0.0.0 is important — without it, the API would be unreachable from outside the container.