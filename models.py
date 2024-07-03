from app import db

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    category = db.Column(db.String(50))
    amount = db.Column(db.Float)
    description = db.Column(db.String(200))