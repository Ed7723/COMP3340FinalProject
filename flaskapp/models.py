from flaskapp import db

# Create a model for items in the inventory. Id used as primary key and the itemname has a max length of 40, has to be unique
# and can't be null. Price is represented as as tring and can't be null.
class Item(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(40),unique = True,nullable = False)
    price = db.Column(db.Float(10),nullable = False)

    def __repr__(self):
        return f"Item:('{self.name}, price: {self.price})"
