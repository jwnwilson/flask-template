import config
from db import db
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from resources.user import User, UserRegister
from swagger import setup_swagger


def create_app():
    app = Flask(__name__)
    api = Api(app)
    jwt = JWTManager(app)
    swagger = setup_swagger(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = config.postgresqlConfig
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # Setup the Flask-JWT-Extended extension
    app.config["JWT_SECRET_KEY"] = config.secret_key  # Change this!
    app.config["PROPAGATE_EXCEPTIONS"] = True

    db.init_app(app)

    api.add_resource(Item, "/item/<string:name>")
    api.add_resource(ItemList, "/items")
    api.add_resource(UserRegister, "/register")
    api.add_resource(User, "/user")
    api.add_resource(Store, "/store/<string:name>")
    api.add_resource(StoreList, "/stores")

    swagger.register(Item)
    swagger.register(ItemList)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)  # important to mention debug=True
