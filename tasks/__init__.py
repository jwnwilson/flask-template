import os

from invoke import task

OS = os.name
IS_WIN = OS in ["nt", "Windows"]
IS_UNIX = not IS_WIN

DOCKER_COMPOSE = "docker-compose"
DOCKER_COMPOSE_RUN = '{} run --no-deps --rm api bash -c "{}"'
PROJECT_NAME = "flask_example"
GOOGLE_PROJECT_NAME = "flask-example-319821"
GOOGLE_PROJECT_NAME = f"eu.gcr.io/{GOOGLE_PROJECT_NAME}/{PROJECT_NAME}"


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
    c.run(
        f"docker tag {PROJECT_NAME}:latest {GOOGLE_PROJECT_NAME} {GOOGLE_PROJECT_NAME}:latest"
    )
    c.run(f"docker push {GOOGLE_PROJECT_NAME}:latest")


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
def tf_init(c):
    c.run(f"cd tf && terraform init")


@task
def tf_plan(c):
    c.run(f"cd tf && terraform plan")


@task
def tf_apply(c):
    c.run(f"cd tf && terraform apply")


@task
def tf_destroy(c):
    c.run(f"cd tf && terraform destroy")
