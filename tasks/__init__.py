import os

from invoke import task

OS = os.name
IS_WIN = OS in ["nt", "Windows"]
IS_UNIX = not IS_WIN

DOCKER_COMPOSE = "docker-compose"
DOCKER_COMPOSE_RUN = "{} run api bash -c \"{}\""


def activate_venv(c):
    if IS_WIN:
        c.run(".\\venv\\Scripts\\activate")
    else:
        c.run("source ./venv/scripts/activate")


@task
def build(c):
    activate_venv(c)
    c.run("poetry install")
    c.run(f"{DOCKER_COMPOSE} build")


@task
def run(c):
    c.run(f"{DOCKER_COMPOSE} up")


@task
def test(c):
    c.run(DOCKER_COMPOSE_RUN.format(DOCKER_COMPOSE, "pytest"))


@task
def lint(c):
    activate_venv(c)
    c.run(f"isort . && black .")


@task
def init_db(c):
    c.run(DOCKER_COMPOSE_RUN.format(DOCKER_COMPOSE, "python ./app/commands/init_db.py"))