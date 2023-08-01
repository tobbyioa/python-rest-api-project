from flask import Flask, request 
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt
from models import ItemModel
from sqlalchemy.exc import SQLAlchemyError
from db import db 
from flask_smorest import abort, Blueprint
from schemas import ItemSchema, ItemUpdateSchema



blp = Blueprint("Items", __name__, description="Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @jwt_required()
    @blp.response(200, ItemSchema)
    def get(self,item_id):
       item = ItemModel.query.get_or_404(item_id)
       return item

    @jwt_required()
    def delete(self ,item_id):
        # jwt = get_jwt()
        # if not jwt.get("is_admin"):
        #     abort(401, message="Admin priviledge required")
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item Deleted"},200

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        item = ItemModel.query.get(item_id)
        if item:
            item.name = item_data['name']
            item.price = item_data['price']
        else:
            item = ItemModel(id=item_id, **item_data)
            
        db.session.add(item)
        db.session.commit()

        return item

@blp.route("/items")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()

    @jwt_required()
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item =  ItemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, 'An error occurred while inserting item.')

        return item