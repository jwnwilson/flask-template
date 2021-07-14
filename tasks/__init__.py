import os

from invoke import task

OS = os.name
IS_WIN = OS in ["nt", "Windows"]
IS_UNIX = not IS_WIN

DOCKER_COMPOSE = "docker-compose"
DOCKER_COMPOSE_RUN = '{} run --no-deps --rm api bash -c "{}"'


@task
def activate_venv(c):
    if not os.path.isdir("venv"):
        c.run("virtualenv ./venv")
    if IS_WIN:
        c.run(".\\venv\\Scripts\\activate")
    else:
        c.run("source ./venv/bin/activate")


@task
def python_deps(c):
    activate_venv(c)
    c.run("poetry install")

@task
def build(c):
    c.run(f"{DOCKER_COMPOSE} build")


@task
def deploy(c):
    build(c)
    c.run(f"docker push -t flask-template:latest")


@task
def run(c):
    c.run(f"{DOCKER_COMPOSE} up")


@task
def test(c):
    c.run(DOCKER_COMPOSE_RUN.format(DOCKER_COMPOSE, "pytest"))


@task
def lint(c, check=False):
    activate_venv(c)
    if check:
        c.run(f"isort . && black . --check")
    else:
        c.run(f"isort . && black .")


@task
def init_db(c):
    c.run(DOCKER_COMPOSE_RUN.format(DOCKER_COMPOSE, "python ./app/commands/init_db.py"))
