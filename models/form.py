from flask_wtf import FlaskForm
from wtforms.fields.html5 import TelField
from wtforms import StringField, PasswordField, IntegerField, SelectField
from wtforms.validators import InputRequired, Length, Required


class NewProductForm(FlaskForm):
    productname = StringField("productname", validators=[InputRequired(), Length(max=50,min=2)])
    price = IntegerField("price")

class NewCustomerForm(FlaskForm):
    customername = StringField("customername", validators=[InputRequired(), Length(max=20,min=4)])
    address = StringField("address")
    town_city = StringField("town_city")
    phoneno = TelField("phoneno")

class EditProductForm(FlaskForm):
    productname = SelectField("productname", choices=[], coerce=int)
    price = IntegerField("price")

