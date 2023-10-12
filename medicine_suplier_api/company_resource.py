#  hospital_api/resource.py

from flask import request, make_response, abort
from flask_restful import Resource
from app_init import db
from .models import MedicineCompany, medicineCompanySchema, MedicineCompanyListSchema

class MedicineCompanyListResource(Resource):
    def get(self):
        list = MedicineCompany.query.all()
        return MedicineCompanyListSchema.dump(list)
    
    def post(self): 
        data = request.get_json()
        ndata = medicineCompanySchema.load(data)
        db.session.add(ndata)
        db.session.commit()
        return medicineCompanySchema.dump(ndata), 201


class MedicineCompanyResource(Resource):
    def get(self, id):
        item = MedicineCompany.query.get(id)
        if item is not None:
            return medicineCompanySchema.dump(item)
        else:
            abort(404, f"MedicineCompany with id {id} not found")

    def delete(self, id):
        item = MedicineCompany.query.get(id)
        if item:
            db.session.delete(item)
            db.session.commit()
            return make_response(f"{id} successfully deleted", 200)
        else:
            abort(404, f"MedicineCompany with id {id} not found")


    def put(self, id):
        xdata = MedicineCompany.query.filter(MedicineCompany.id == id).one_or_none()
        if xdata:
            data = medicineCompanySchema.load(request.get_json())
            xdata.name = data.name
            xdata.address = data.address
            xdata.phone = data.phone
            xdata.details = data.details
            xdata.manpower_capacity = data.manpower_capacity
            db.session.merge(xdata)
            db.session.commit()
            return medicineCompanySchema.dump(xdata), 201
        else:
            abort(404, f"MedicineCompany with id {id} not found")
