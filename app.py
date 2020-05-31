import os
from models.form import *
from models.schema import *
from flask_admin import Admin
from flask_bootstrap import Bootstrap
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask import Flask, render_template, send_file, request, url_for, redirect, send_from_directory


app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'my-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'


@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/newProduct", methods=['POST','GET'])
def newProduct():
    form = NewProductForm()
    if form.validate_on_submit():

        newProduct = Product(name=form.productname.data,
                            price=form.price.data)
        db.session.add(newProduct)
        db.session.commit()

    return render_template("newproduct.html",form=form)

@app.route("/editProduct", methods=['POST','GET'])
def editProduct():
    form = EditProductForm()
    product = db.session.query(Product).all()
    form.productname.choices = [(iteam.id,iteam.name) for iteam in product]

    if form.validate_on_submit():
        product = Product.query.filter_by(id=form.productname.data).first()
        product.price = form.price.data
        db.session.commit()

    return render_template("editproduct.html", form=form)

@app.route("/newCustomer", methods=['POST','GET'])
def newCustomer():
    form = NewCustomerForm()
    if form.validate_on_submit():
        newCustomer = Customer(name=form.customername.data,
                                town_city=form.town_city.data,
                                address=form.address.data,
                                phone=form.phoneno.data)
        db.session.add(newCustomer)
        db.session.commit()

    return render_template("newcustomer.html",
                            form=form)

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
	from db import db
	db.init_app(app)
	app.run(debug=True)