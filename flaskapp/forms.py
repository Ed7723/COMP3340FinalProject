from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

# Class inherits from base FlaskForm and creates 3 new parameters: itemName, itemPrice and a submit button 
# itemName and itemPrice and validated so that they are required field and itemName has 40 char limit and itemPrice has 10
class createForm(FlaskForm):
    itemName = StringField('itemName',validators =[DataRequired(),Length(max=40)])
    itemPrice = StringField('itemPrice',validators =[DataRequired(),Length(max=10)])
    submit = SubmitField('Add item')

    def validate_item(self,itemName):
        item = Item.query.filter_by(name = itemName.data).first()
        if item:
            raise ValidationError("Item already exists in the database")