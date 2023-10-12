#  hospital_api/resource.py

from flask import request, make_response, abort
from flask_restful import Resource
from app_init import db
from .models import MedicineGenerType, medicineGenerTypeSchema, medicineGenerTypeListSchema

class MedicineGenerTypeListResource(Resource):
    def get(self):
        list = MedicineGenerType.query.all()
        return medicineGenerTypeListSchema.dump(list)
    
    def post(self): 
        data = request.get_json()
        ndata = medicineGenerTypeSchema.load(data)
        db.session.add(ndata)
        db.session.commit()
        return medicineGenerTypeSchema.dump(ndata), 201


class MedicineGenerTypeResource(Resource):
    def get(self, id):
        item = MedicineGenerType.query.get(id)
        if item is not None:
            return medicineGenerTypeSchema.dump(item)
        else:
            abort(404, f"MedicineGenerType with id {id} not found")

    def delete(self, id):
        item = MedicineGenerType.query.get(id)
        if item:
            db.session.delete(item)
            db.session.commit()
            return make_response(f"{id} successfully deleted", 200)
        else:
            abort(404, f"MedicineGenerType with id {id} not found")


    def put(self, id):
        xdata = MedicineGenerType.query.filter(MedicineGenerType.id == id).one_or_none()
        if xdata:
            data = medicineGenerTypeSchema.load(request.get_json())
            xdata.name = data.name
            xdata.details = data.details
            db.session.merge(xdata)
            db.session.commit()
            return medicineGenerTypeSchema.dump(xdata), 201
        else:
            abort(404, f"MedicineGenerType with id {id} not found")
