from marshmallow import Schema, fields


class ItemSerializer(Schema):
    name = fields.Str()
    price = fields.Float()
