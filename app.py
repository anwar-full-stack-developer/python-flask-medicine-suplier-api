import app_init
db=app_init.db
app=app_init.app
api = app_init.api


# Create the endpoints.
from medicine_suplier_api.resource import  MedicineGenerTypeListResource, MedicineGenerTypeResource
from medicine_suplier_api.pot_type_resource import MedicinePotTypeResource, MedicinePotTypeListResource
from medicine_suplier_api.company_resource import MedicineCompanyResource, MedicineCompanyListResource
from medicine_suplier_api.medicine_resource import MedicineListResource, MedicineResource


#  api routes (medicine_suplier)
api.add_resource(MedicineGenerTypeListResource, '/medicine_suplier/geners')
api.add_resource(MedicineGenerTypeResource, '/medicine_suplier/gener/<id>')

api.add_resource(MedicinePotTypeListResource, '/medicine_suplier/pots')
api.add_resource(MedicinePotTypeResource, '/medicine_suplier/pot/<id>')

api.add_resource(MedicineCompanyListResource, '/medicine_suplier/companies')
api.add_resource(MedicineCompanyResource, '/medicine_suplier/company/<id>')

api.add_resource(MedicineListResource, '/medicine_suplier/medicines')
api.add_resource(MedicineResource, '/medicine_suplier/medicine/<id>')



if __name__ == '__main__':
    # Create the database tables.
    with app.app_context():
        db.create_all()
    # Start the Flask development web server.
    app.run(host="0.0.0.0", port=8000, debug=True)
