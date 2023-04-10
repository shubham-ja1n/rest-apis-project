import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import StoreModel
from schemas import StoreSchema

blp = Blueprint("stores",__name__,description="Operations on stores")

@blp.route("/store/<int:store_id>/")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store
        # try:
        #     return stores[store_id]
        # except KeyError:
        #     abort(404, message = "Store not found.")

    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"messgae": "Store deleted."}
        # try:
        #     del stores[store_id]
        #     return {"messgae": "Store deleted."}
        # except KeyError:
        #     abort(404, message ="Store not found.")

@blp.route("/store/")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()
        # return stores.values()

    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A store with that name already exists."
            )
        except SQLAlchemyError:
            abort(500, messgae="An error occured creating the store.")
        
        return store
        # store_data = request.get_json()
        # if(
        #     "name" not in store_data
        # ):
        #     abort(
        #         400,
        #         message="Bad request. Ensure 'name' is included in the JSON payload." 
        #     )
        # for store in stores.values():
        #     if(
        #         store["name"] == store_data["name"]
        #     ):
        #         abort(
        #             400,
        #             message="Store already exists."
        #         )
        # store_id = uuid.uuid4().hex
        # new_store = {**store_data, "id":store_id}
        # stores[store_id] = new_store
        # return new_store