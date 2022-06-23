# FastAPI

## Project structure

```
/fast_api -> src code
  /models -> models
    __init__.py -> export all models here
  /routers -> routes
  /utils -> utils and helpers
  main.py -> entry point for FastAPI server
  settings.py -> settings and configuration
```

## Swagger documentation

Go to [http://localhost:8000/docs](http://localhost:8000/docs) to see the documentation.

## Commands

```shell
# install dependencies
poetry install

# resync with pyproject.toml
poetry update

# add package
poetry add <package>

# remove package
poetry remove <package>

# run the server on localhost:8000
poetry run start
```

## Docker Image

> default port: 8000