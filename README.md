# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). 
Find the value for the following keys:
Set the  .env file.

###Running the todo-app in kubernetees#######
Step 1: Run minikube start in an admin terminal to spin up your minikube cluster to run kubernetees in your local

Step 2: Build the image with the following command docker build --target production --tag todo-app:prod .

Step 3: Run minikube image load todo-app:prod 

Step 4: Run kubectl apply -f service.yaml  

Step 5: Run kubectl apply -f service.yaml

Step 6: To spin the applicaiton run kubectl port-forward service/todo-app 7080:7080 


###TroubleShotting:####

kubectl get pods

kubectl logs <my-pod>

minikube --help



## set .env.test

CLIENT_ID: create clietn_id in git hub using new url : https://todo-app-kamol.azurewebsites.net/ from the azure app
CLIENT_SECRET : retrieve the secret as well 



## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

