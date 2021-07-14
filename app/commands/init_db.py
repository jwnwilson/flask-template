def create_tables():
    from app import app, db

    db.create_all(app=app)
    print("Created initial DB tables")


if __name__ == "__main__":
    create_tables()
