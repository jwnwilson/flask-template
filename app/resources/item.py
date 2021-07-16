from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_restful import reqparse
from serializers.item import ItemSerializer
from util.logs import create_logger


class Item(
    MethodResource,
):
    parser = reqparse.RequestParser()

    def __init__(self):
        self.logger = create_logger()

    @doc(description="Get Items.", tags=["item"])
    @marshal_with(ItemSerializer)
    def get(self):
        """Items in the store"""
        item = {"name": "item"}

        # Domain level logic goes here

        self.logger.info(f"returning item: {item}")
        if item:
            return item
        return {"message": "Item not found"}, 404


class ItemList(MethodResource):
    @doc(description="Get Items.", tags=["item"])
    @marshal_with(ItemSerializer(many=True))
    def get(self):
        return [{"name": "item"}]
