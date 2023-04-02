from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

# Class inherits from base FlaskForm and creates 3 new parameters: itemName, itemPrice and a submit button 
# itemName and itemPrice and validated so that they are required field and itemName has 40 char limit and itemPrice has 10
class createForm(FlaskForm):
    itemName = StringField('itemName',validators =[DataRequired(),Length(max=40)])
    itemPrice = StringField('itemPrice',validators =[DataRequired(),Length(max=10)])
    submit = SubmitField('Add item')