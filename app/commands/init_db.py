def create_tables():
    from app import db, app

    db.create_all(app=app)
    print("Created initial DB tables")


if __name__ == "__main__":
    create_tables()