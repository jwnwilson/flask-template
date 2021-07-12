# using python slim as a reliable base image
FROM python:3.9-slim

# Create a folder to copy project to and work in
WORKDIR /app

# install requirements
COPY poetry.lock pyproject.toml ./
RUN pip3 install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction

# Copy project after installing requirements to speed up build
COPY . .

EXPOSE 5000

# Default to production values for when we deploy this container
ENV FLASK_APP=app/app.py
ENV FLASK_ENV=production
ENV FLASK_DEBUG=0
ENV PYTHONPATH=/app/app

CMD ["gunicorn","-b", "0.0.0.0:5000", "-w", "4", "-k", "gevent", "--worker-tmp-dir", "/dev/shm", "app/app"]
