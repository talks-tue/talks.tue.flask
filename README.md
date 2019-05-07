# talks.tue
A webapp to manage talks and more at the Eberhard Karls University of Tübingen.

## Dependecies
1. [docker](https://www.docker.com/) for containerization
2. [docker-compose](https://github.com/docker/compose) for container orchastration

## Usage
1. run `docker-compose build` (this will take some time)
2. run `docker-compose up` (this will open HTTP and HTTPS ports to your network)

## Development
1. install [pipenv](https://pypi.org/project/pipenv/) and python 3.7.
2. run `pipenv install --dev` (this can take some time)
3. set `COMPOSE_FILE` in `.env` to `dev.yml`
2. run `docker-compose build` (this will take some time)
3. run `docker-compose up`

## Creating a superuser
Simply run `make auth_createsuperuser` and fill out the prompts.

## Applying migrations
Run `make db_upgrade` and you should be golden.

## What else can `make` do for me?
Just run `make` and it will tell you. ;)
