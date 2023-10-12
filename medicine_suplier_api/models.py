from app_init import db, mar

# allopathy, homeopathy, unani, ayurvedic, Herbal
class MedicineGenerType(db.Model):
    __tablename__ = "medicine_gener_types"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    details = db.Column(db.String(255)) # optional

class MedicineGenerTypeSchema(mar.SQLAlchemyAutoSchema):
    id = mar.auto_field()

    class Meta:
        model = MedicineGenerType
        fields = ("id", "name", "details")
        load_instance = True


medicineGenerTypeSchema = MedicineGenerTypeSchema()
medicineGenerTypeListSchema = MedicineGenerTypeSchema(many=True)


# paper box, jar, tube, bottle, tablet, injection
class MedicinePotType(db.Model):
    __tablename__ = "medicine_pot_types"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    details = db.Column(db.String(255)) # optional

class MedicinePotTypeSchema(mar.SQLAlchemyAutoSchema):
    id = mar.auto_field()

    class Meta:
        model = MedicinePotType
        fields = ("id", "name", "details")
        load_instance = True


medicinePotTypeSchema = MedicinePotTypeSchema()
medicinePotTypeListSchema = MedicinePotTypeSchema(many=True)


class MedicineCompany(db.Model):
    __tablename__ = "medicine_company"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    address = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    details = db.Column(db.String(255)) # optional
    # supplier and wholesale records
    manpower_capacity =  db.Column(db.Integer)

class MedicineCompanySchema(mar.SQLAlchemyAutoSchema):
    id = mar.auto_field()

    class Meta:
        model = MedicineCompany
        fields = ("id", "name", "address", "phone", "details", "manpower_capacity")
        load_instance = True


medicineCompanySchema=MedicineCompanySchema()
MedicineCompanyListSchema=MedicineCompanySchema(many=True)


class Medicine(db.Model):
    __tablename__ = "medicines"

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String)
    name = db.Column(db.String(255))
    unit = db.Column(db.String(255)) # mg, ml, pics
    details = db.Column(db.String(255)) # optional

    # supplier and wholesale records
    quantity = db.Column(db.Integer)
    min_order_quantity = db.Column(db.Integer)
    max_order_quantity = db.Column(db.Integer)
    weekly_production_capacity = db.Column(db.Integer)
    monthly_production_capacity = db.Column(db.Integer)
    country_to_ship = db.Column(db.String)


    company_id = db.Column(db.Integer, db.ForeignKey('medicine_company.id'))
    company = db.relationship("MedicineCompany", backref="medicines", lazy="select")

    gener_type_id = db.Column(db.Integer, db.ForeignKey('medicine_gener_types.id'))
    gener_type = db.relationship("MedicineGenerType", backref="medicines", lazy="select")

    pot_type_id = db.Column(db.Integer, db.ForeignKey('medicine_pot_types.id'))
    pot_type = db.relationship("MedicinePotType", backref="medicines", lazy="select")


class MedicineSchema(mar.SQLAlchemyAutoSchema):
    id = mar.auto_field()
    company = mar.auto_field()
    gener_type = mar.auto_field()
    pot_type = mar.auto_field()

    class Meta:
        model = Medicine
        fields = ("id", "image", "name", "unit", 
                  "details", "company_id", "company", "gener_type_id", "gener_type", 
                  "pot_type_id", "pot_type", "quantity", 
                  "min_order_quantity", "max_order_quantity", "weekly_production_capacity", 
                  "monthly_production_capacity", "country_to_ship"
                  )
        load_instance = True


medicineSchema = MedicineSchema()
medicineListSchema = MedicineSchema(many=True)
