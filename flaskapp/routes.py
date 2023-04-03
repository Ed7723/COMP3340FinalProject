from flask import render_template,flash,redirect,url_for
from flaskapp import app,db
from flaskapp.forms import createForm
from flaskapp.models import Item

# Home route, renders home.html
@app.route("/")
def home():
    return render_template("home.html", title = 'Homepage')

# Create route, renders create.html. Allows get and post for creating items
# Post method will use form created from forms.py and then validate it. If successful, will flash a message and 
# then redirect to view page.
@app.route("/create",methods = ['GET','POST'])
def create():
    form = createForm()
    if form.validate_on_submit():
        item = Item(name = form.itemName.data, price = form.itemPrice.data)
        db.session.add(item)
        db.session.commit()
        flash(f'Sucessfully created new item: {form.itemName.data}','success')
        return redirect(url_for('view'))
    return render_template("create.html", title = 'Create Items',form=form)

# View route, renders view.html. Allows looking at items.
@app.route("/view")
def view():
    itemList = Item.query.all()
    return render_template("view.html", title = 'View Items' , items = itemList)