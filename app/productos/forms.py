from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class NewProductFrom(FlaskForm):
    nombre = StringField('ingrese producto')
    precio = StringField("ingrese precio")
    submit = SubmitField("Registrar")