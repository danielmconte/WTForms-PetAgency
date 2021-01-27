from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired


class AddPetForm(FlaskForm):

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog','Dog'), ('porc', 'Porcupine')], validators=[InputRequired()])
    photo_url = StringField("Image URL")
    age = StringField("Age")
    notes = TextAreaField("Notes")
