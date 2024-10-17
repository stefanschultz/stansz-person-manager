# PERSON MANAGER
This is a simple template project for managing people. It is a simple CRUD application that allows you to add, edit, delete and view people. It is built using the following technologies:
- Python
- FastAPI
- SQLite
- Docker / Docker Compose
- Nginx

## Prerequisites

- Install [Docker](https://docs.docker.com/get-docker/)
- Install [Docker Compose](https://docs.docker.com/compose/install/)

## Project Structure

The directory structure of the application should look like this:

```
nginx-fastapi-project/
├── app/
    │
    ├── main.py
    │
    ├── database.py
    │
    ├── models.py
    │
    ├── crud.py
    │
    ├── templates/
        │
        ├── base.html
        │
        ├── index.html
        │
        └── add_person.html
    │
    ├── database_storage/
        │
        └── stansz_person_manager.db
│
├── docker-compose.yml
│
├── Dockerfile
│
├── nginx.conf
│
└── requirements.conf
```


## Starting the Application

To start the application, follow these steps in the project directory:

1. **Build the containers and start the project:**

   ```bash
   docker-compose up --build
    ```
   
This command creates and starts the Docker containers (FastAPI and Nginx) based on the configurations in the docker-compose.yml and Dockerfile. The --build flag ensures that the containers are rebuilt.

Access the application:

Open a web browser and go to http://localhost:8000 to access the application.

## Stopping the Application

    ```bash
    docker-compose down
    ```

This command stops all running containers and removes them.

## Starting the Application in Detached Mode

If you want to start the application in the background (without showing logs in the terminal), you can use:

    ```bash
    docker-compose up --build -d
    ```

The `-d` flag runs the application in detached mode (in the background).

## Restarting the Application

If you made changes to the code and want to rebuild and restart the application, use the following commands:

    ```bash
    docker-compose down
    docker-compose up --build
    ```
This stops the containers, rebuilds the application, and restarts it.

## Viewing Logs and Debugging

To view the logs of the running containers, use the command:

    ```bash
    docker-compose logs -f
    ```

The `-f` flag streams the logs in real-time.

## Notes

Make sure that the necessary files like `Dockerfile`, `docker-compose.yml`, and the Python modules (see `requirements.txt`) are correctly configured before starting the application.


This is a complete guide for starting, stopping, and managing your Dockerized FastAPI application with Nginx.
