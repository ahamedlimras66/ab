import datetime
from db import db
from flask_login import UserMixin
from sqlalchemy import ForeignKey


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price =  db.Column(db.Integer, nullable=False)
    bill = db.relationship('Bill',cascade="all,delete",backref="product")

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    town_city = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    bill = db.relationship('Bill',cascade="all,delete",backref="customer")


class Bill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice_no = db.Column(db.Integer, nullable=False)
    customer_id = db.Column(db.Integer, ForeignKey('product.id'))
    product_id = db.Column(db.Integer, ForeignKey('customer.id'))
    bill_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)