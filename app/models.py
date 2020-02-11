from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Temperature(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employeeId = db.Column(db.String(30))
    temperature = db.Column(db.Float)
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)

    def __init__(self, employeeId, temperature, createdAt, updatedAt):
        self.employeeId = employeeId
        self.temperature = temperature
        self.createdAt = createdAt
        self.updatedAt = updatedAt
