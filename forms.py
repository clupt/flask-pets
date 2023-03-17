"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, URL, AnyOf

class AddPetForm(FlaskForm):
    """Form for adding a pet"""

    name = StringField("Pet Name",
                       validators=[InputRequired(message="Please include a Pet Name"), ])

    species = StringField("Pet Species, in latin please",
                          validators=[AnyOf(["cat", "Cat", "dog", "Dog", "porcupine", "Porcupine"], message="Please include a valid species")])

    photo_url = StringField("Include a photo of the pet",
                            validators=[URL(require_tld=False,
                            message="Please include an image of the pet"),
                            Optional()])

    # photo_url = StringField("Include a photo of your pet")

    age = SelectField("Pick a stage of life for your pet",
                        choices=[("baby", "Baby"), ("young", "Young"),
                               ("adult", "Adult"), ("senior", "Senior")],
                        validators=[InputRequired(message="Please select an option")]
                    )
    notes = StringField("Tell us a little about your pet",
                        validators=[Optional()])