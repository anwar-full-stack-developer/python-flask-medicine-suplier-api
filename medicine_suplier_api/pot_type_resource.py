#  hospital_api/resource.py

from flask import request, make_response, abort
from flask_restful import Resource
from app_init import db
from .models import MedicinePotType, medicinePotTypeSchema, medicinePotTypeListSchema

class MedicinePotTypeListResource(Resource):
    def get(self):
        list = MedicinePotType.query.all()
        return medicinePotTypeListSchema.dump(list)
    
    def post(self): 
        data = request.get_json()
        ndata = medicinePotTypeSchema.load(data)
        db.session.add(ndata)
        db.session.commit()
        return medicinePotTypeSchema.dump(ndata), 201


class MedicinePotTypeResource(Resource):
    def get(self, id):
        item = MedicinePotType.query.get(id)
        if item is not None:
            return medicinePotTypeSchema.dump(item)
        else:
            abort(404, f"MedicinePotType with id {id} not found")

    def delete(self, id):
        item = MedicinePotType.query.get(id)
        if item:
            db.session.delete(item)
            db.session.commit()
            return make_response(f"{id} successfully deleted", 200)
        else:
            abort(404, f"MedicinePotType with id {id} not found")


    def put(self, id):
        xdata = MedicinePotType.query.filter(MedicinePotType.id == id).one_or_none()

        if xdata:
            data = medicinePotTypeSchema.load(request.get_json())
            xdata.name = data.name
            xdata.details = data.details
            db.session.merge(xdata)
            db.session.commit()
            return medicinePotTypeSchema.dump(xdata), 201
        else:
            abort(404, f"MedicinePotType with id {id} not found")
