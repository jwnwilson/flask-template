postgresql = {
    "host": "database",
    "user": "postgres",
    "passwd": "magical_password",
    "db": "db",
}

postgresqlConfig = "postgresql+psycopg2://{}:{}@{}/{}".format(
    postgresql["user"], postgresql["passwd"], postgresql["host"], postgresql["db"]
)
