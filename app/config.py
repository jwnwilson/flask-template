postgresql = {
    "host": "database",
    "user": "postgres",
    "passwd": "password",
    "db": "flask-template",
}

postgresqlConfig = "postgresql+psycopg2://{}:{}@{}/{}".format(
    postgresql["user"], postgresql["passwd"], postgresql["host"], postgresql["db"]
)
