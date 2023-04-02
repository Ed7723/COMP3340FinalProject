from flask import Flask, render_template,flash,redirect,url_for
from forms import createForm
app = Flask(__name__)
# Config for security. Secret key is used for secure signin for session cookies.
app.config['SECRET_KEY'] = '23d7a1eda8fff64969fac5ebce9d7d92'


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
        flash(f'Sucessfully created new item: {form.itemName.data}','success')
        return redirect(url_for('view'))
    return render_template("create.html", title = 'Create Items',form=form)

# View route, renderes view.html. Allows looking at items.
@app.route("/view")
def view():
    return render_template("view.html", title = 'View Items')