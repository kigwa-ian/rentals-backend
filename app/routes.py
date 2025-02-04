from flask import Blueprint, jsonify, request, render_template
from app.models import Tenant, Apartment, RentPayment, db, ma  # Import Marshmallow instance

# Create the blueprint for the app
main_routes = Blueprint('main', __name__)

# Instantiate the Marshmallow schemas
class TenantSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Tenant

    id = ma.auto_field()
    name = ma.auto_field()
    apartment_id = ma.auto_field()

class ApartmentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Apartment

    id = ma.auto_field()
    number = ma.auto_field()

class RentPaymentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = RentPayment

    id = ma.auto_field()
    amount = ma.auto_field()
    paid = ma.auto_field()
    tenant_id = ma.auto_field()

tenant_schema = TenantSchema()
tenants_schema = TenantSchema(many=True)  # For multiple items
apartment_schema = ApartmentSchema()
apartments_schema = ApartmentSchema(many=True)
rent_payment_schema = RentPaymentSchema()
rent_payments_schema = RentPaymentSchema(many=True)

# Tenant Routes
@main_routes.route('/tenants', methods=['GET', 'POST'])
def handle_tenants():
    if request.method == 'POST':
        data = request.json
        new_tenant = Tenant(name=data['name'], apartment_id=data['apartment_id'])
        db.session.add(new_tenant)
        db.session.commit()
        return tenant_schema.dump(new_tenant), 201
    tenants = Tenant.query.all()
    return jsonify(tenants_schema.dump(tenants))  # Use `tenants_schema`

# Apartment Routes
@main_routes.route('/apartments', methods=['GET', 'POST'])
def handle_apartments():
    if request.method == 'POST':
        data = request.json
        new_apartment = Apartment(number=data['number'])
        db.session.add(new_apartment)
        db.session.commit()
        return apartment_schema.dump(new_apartment), 201
    apartments = Apartment.query.all()
    return jsonify(apartments_schema.dump(apartments))  # Use `apartments_schema`

# Rent Payment Routes
@main_routes.route('/payments', methods=['GET', 'POST'])
def handle_payments():
    if request.method == 'POST':
        data = request.json
        new_payment = RentPayment(amount=data['amount'], paid=data['paid'], tenant_id=data['tenant_id'])
        db.session.add(new_payment)
        db.session.commit()
        return rent_payment_schema.dump(new_payment), 201
    payments = RentPayment.query.all()
    return jsonify(rent_payments_schema.dump(payments))  # Use `rent_payments_schema`

# Home Route (Rendered HTML)
@main_routes.route('/')
def home():
    return render_template('home.html')
