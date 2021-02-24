# sweepsouth-api

A api for exchange rates written in python 

## To run

The app uses docker [docker](https://www.docker.com/products/docker-desktop), to run the app execute

```bash
docker-compose up --build
```

To run the app tests execute
```bash
docker exec { app_container_id } pytest -v
```

## Stack

- [Docker](https://www.docker.com/products/docker-desktop)
  - Allows for easy collaboration and deployment on projects because the `env` doesn't change from machine to machine  
- [Fastapi](https://fastapi.tiangolo.com)
  - Allows for fast api development
  - Comes with docs baked in
  - Supports async out of the box
- [Postgresql](https://www.postgresql.org/)
