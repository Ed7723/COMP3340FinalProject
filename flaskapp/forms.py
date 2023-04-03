from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from flaskapp.models import Item

class createForm(FlaskForm):
    itemName = StringField('itemName',validators =[DataRequired(),Length(max=40)])
    itemPrice = StringField('itemPrice',validators =[DataRequired(),Length(max=10)])
    submit = SubmitField('Add item')

    def validate_item(self, itemName):
        item = Item.query.filter_by(name = itemName.data).first()
        if item:
            raise ValidationError("Item already exists in the database")

    def validate_itemPrice(self, itemPrice):
        if not itemPrice.data.isnumeric():
            raise ValidationError("Item's price value must be a number")
        
class editForm(FlaskForm):
    itemName = StringField('itemName', validators=[DataRequired(), Length(max=40)])
    itemPrice = StringField('itemPrice', validators=[DataRequired(), Length(max=10)])
    submit = SubmitField('Edit item')

    def validate_item(self, itemName):
        item = Item.query.filter_by(name=itemName.data).first()
        if item:
            raise ValidationError("Item already exists in the database")

    def validate_itemPrice(self, itemPrice):
        try:
            float(itemPrice.data)
        except ValueError:
            raise ValidationError("Item's price value must be a number")
