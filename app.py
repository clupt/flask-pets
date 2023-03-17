"""Flask app for adopt app."""

from flask import Flask, flash, redirect, render_template

from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.route('/add', methods=["GET", "POST"])
def show_or_add_pet_add_form():
    """On GET, show pet add form. On POST, add pet data to db"""


    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url,
                      age=age, notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {name} the {species}")
        return redirect('/')
    else:
        return render_template('/add', form=form)








