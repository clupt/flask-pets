"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import TextField, StringField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, Email, URL

class AddPetForm(FlaskForm):
    """Form for adding a pet"""

    name = StringField("Pet Name", validators=[InputRequired(message="Please include a Pet Name"), ])
    species = StringField("Pet Species, in latin please",
                          validators=[InputRequired(message="Please include a species")])
    photo_url = StringField("Include a photo of the pet",
                            validators=[URL(require_tld=False, message="Please include an image of the pet" )])
    age = SelectField("Pick a stage of life for your pet",
                      choices=[("baby", "Baby"), ("young", "Young"),
                               ("adult", "Adult"), ("senior", "Senior")], validators=[InputRequired(message="Please select an option")]
                    )
    notes = StringField("Tell us a little about your pet", validators=[Optional()])