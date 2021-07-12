from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_apispec.extension import FlaskApiSpec

from app.config import postgresqlConfig
from app.resources.item import Item, ItemList
from app.resources.store import Store, StoreList
from app.resources.user import User, UserRegister
from app.swagger import setup_swagger

app = Flask(__name__)
api = Api(app)
jwt = JWTManager(app)
swagger = setup_swagger(app)

app.config["SQLALCHEMY_DATABASE_URI"] = postgresqlConfig
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "Dese.Decent.Pups.BOOYO0OST"  # Change this!

@app.before_first_request
def create_tables():
    from app.db import db

    db.init_app(app)
    db.create_all()


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")
api.add_resource(User, "/user")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")

swagger.register(Item)
swagger.register(ItemList)

if __name__ == "__main__":
    app.run(debug=True)  # important to mention debug=True
