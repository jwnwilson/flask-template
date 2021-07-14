from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_jwt_extended import jwt_required
from flask_restful import reqparse
from models.item import ItemModel
from serializers.item import ItemSerializer
from util.logs import create_logger


class Item(
    MethodResource,
):
    parser = (
        reqparse.RequestParser()
    )  # only allow price changes, no name changes allowed
    parser.add_argument(
        "price", type=float, required=True, help="This field cannot be left blank"
    )
    parser.add_argument(
        "store_id", type=int, required=True, help="Must enter the store id"
    )

    def __init__(self):
        self.logger = create_logger()

    @jwt_required()
    @doc(description="Get Items.", tags=["item"])
    @marshal_with(ItemSerializer)
    def get(self, name):
        """Items in the store"""
        item = ItemModel.find_by_name(name)
        self.logger.info(f"returning item: {item.json()}")
        if item:
            return item.json()
        return {"message": "Item not found"}, 404

    @jwt_required()
    @doc(description="Get Items.", tags=["item"])
    @marshal_with(ItemSerializer)
    def post(self, name):
        self.logger.info(f"parsed args: {Item.parser.parse_args()}")

        if ItemModel.find_by_name(name):
            return {
                "message": "An item with name '{}' already exists.".format(name)
            }, 400
        data = Item.parser.parse_args()
        item = ItemModel(name, data["price"], data["store_id"])

        try:
            item.save()
        except:
            return {"message": "An error occurred inserting the item."}, 500
        return item.json(), 201

    @jwt_required()
    @doc(description="Get Items.", tags=["item"])
    @marshal_with(ItemSerializer)
    def delete(self, name):

        item = ItemModel.find_by_name(name)
        if item:
            item.delete()

            return {"message": "item has been deleted"}

    @jwt_required()
    @doc(description="Get Items.", tags=["item"])
    @marshal_with(ItemSerializer)
    def put(self, name):
        # Create or Update
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, data["price"])
        else:
            item.price = data["price"]

        item.save()

        return item.json()


class ItemList(MethodResource):
    @jwt_required()
    @doc(description="Get Items.", tags=["item"])
    @marshal_with(ItemSerializer(many=True))
    def get(self):
        return {"items": [item.json() for item in ItemModel.query.all()]}
