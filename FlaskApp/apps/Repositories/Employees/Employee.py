from datetime import date
from FlaskApp import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=False, unique=True)
    images = db.Column(db.String(200), nullable=True)
    gender = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"Employee('{self.title}', '{self.date_employee}')"