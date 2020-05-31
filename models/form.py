from flask_wtf import FlaskForm
from wtforms.fields.html5 import TelField
from wtforms import StringField, PasswordField, IntegerField, SelectField
from wtforms.validators import InputRequired, Length, Required


class NewProductForm(FlaskForm):
    productname = StringField(validators=[InputRequired(), Length(max=50,min=2)])
    price = IntegerField()

class NewCustomerForm(FlaskForm):
    customername = StringField(validators=[InputRequired(), Length(max=20,min=4)])
    address = StringField()
    town_city = StringField()
    phoneno = TelField()

class EditProductForm(FlaskForm):
    productname = SelectField(choices=[], coerce=int)
    price = IntegerField()

