from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize the SQLAlchemy and Marshmallow instances
db = SQLAlchemy()
ma = Marshmallow()  # Define Marshmallow instance

# Define the models (Tenant, Apartment, RentPayment)

class Apartment(db.Model):
    __tablename__ = 'apartments'  # Explicit table name
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20), nullable=False, unique=True)
    tenants = db.relationship('Tenant', backref='apartment', lazy=True, cascade="all, delete")

class Tenant(db.Model):
    __tablename__ = 'tenants'  # Explicit table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    apartment_id = db.Column(db.Integer, db.ForeignKey('apartments.id', ondelete="CASCADE"), nullable=False)
    payments = db.relationship('RentPayment', backref='tenant', lazy=True, cascade="all, delete")

class RentPayment(db.Model):
    __tablename__ = 'rent_payments'  # Explicit table name
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    paid = db.Column(db.Boolean, default=False)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id', ondelete="CASCADE"), nullable=False)

# Define Marshmallow schemas for serialization
class TenantSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tenant
        include_fk = True  # Include foreign keys

class ApartmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Apartment

class RentPaymentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RentPayment
        include_fk = True  # Include foreign keys
