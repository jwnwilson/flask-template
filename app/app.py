import config
from flask import Flask
from flask_restful import Api
from resources.item import Item, ItemList
from swagger import setup_swagger


def create_app():
    app = Flask(__name__)
    api = Api(app)
    swagger = setup_swagger(app)

    # Setup the Flask-JWT-Extended extension
    app.config["JWT_SECRET_KEY"] = config.secret_key  # Change this!
    app.config["PROPAGATE_EXCEPTIONS"] = True

    api.add_resource(Item, "/item")
    api.add_resource(ItemList, "/items")

    swagger.register(Item)
    swagger.register(ItemList)

    return app


app = create_app()


if __name__ == "__main__":

    app.run(debug=True)  # important to mention debug=True
