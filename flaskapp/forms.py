from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length, ValidationError,InputRequired
from flaskapp.models import Item

class createForm(FlaskForm):
    itemName = StringField('itemName',validators =[DataRequired(),Length(max=40)])
    itemPrice = FloatField('itemPrice',validators =[InputRequired()])
    submit = SubmitField('Add item')

    def validate_itemName(self, itemName):
        item = Item.query.filter_by(name = itemName.data).first()
        if item:
            raise ValidationError("Item already exists in the database")

    def validate_itemPrice(self, itemPrice):
        isNumeric = isinstance(itemPrice.data,float)
        if not isNumeric:
            raise ValidationError("Item's price value must be a number")
        
class editForm(FlaskForm):
    itemName = StringField('itemName', validators=[DataRequired(), Length(max=40)])
    itemPrice = FloatField('itemPrice',validators =[InputRequired()])
    submit = SubmitField('Edit item')

    def validate_itemPrice(self, itemPrice):
        isNumeric = isinstance(itemPrice.data,float)
        if not isNumeric:
            raise ValidationError("Item's price value must be a number")
