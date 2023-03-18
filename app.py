"""Flask app for adopt app."""

from flask import Flask, flash, redirect, render_template

from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db, Pet
from forms import AddPetForm, EditPetForm

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


@app.get('/')
def show_homepage():
    """Shows the homepage"""

    pets = Pet.query.all()

    return render_template("base.html", pets=pets)


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

        new_pet = Pet(
            name=name, species=species, photo_url=photo_url,
                      age=age, notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {name} the {species}")
        return redirect('/')
    else:
        return render_template('add.html', form=form)


@app.route('/edit/<int:id>', methods=["GET", "POST"])
def show_edit_page(id):
    """Show edit page on GET, or Edit Pet info on POST"""
    pet = Pet.query.get_or_404(id)

    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = (form.available.data)

        db.session.commit()

        flash(f"Edited {pet.name} the {pet.species}")
        return redirect('/')
    else:
        return render_template("edit.html", form=form, pet=pet)
