from flask import render_template,flash,redirect,url_for
from flaskapp import app,db
from flaskapp.forms import createForm, editForm
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

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit(item_id):
    item = Item.query.get_or_404(item_id)
    form = editForm(itemName=item.name, itemPrice=item.price)
    if form.validate_on_submit():
        item.name = form.itemName.data
        item.price = form.itemPrice.data
        db.session.commit()
        flash(f'Item \'{form.itemName.data}\' was updated successfully', 'success')
        return redirect(url_for('view'))
    return render_template('edit.html' ,title = 'Edit Items', item=item, form=form)

@app.route('/delete/<int:item_id>', methods=['POST'])
def delete(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash(f'Item \'{item.name}\' was deleted successfully', 'success')
    return redirect(url_for('view'))