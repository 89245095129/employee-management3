from app import db

class Position(db.Model):
    __tablename__ = 'positions'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    
    employees = db.relationship('Employee', backref='position', lazy=True)

class Employee(db.Model):
    __tablename__ = 'employees'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    position_id = db.Column(db.Integer, db.ForeignKey('positions.id'), nullable=False)
    hire_date = db.Column(db.Date, nullable=False)
    salary = db.Column(db.Numeric(10, 2), nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    
    subordinates = db.relationship(
        'Employee', 
        backref=db.backref('manager', remote_side=[id]),
        lazy=True
    )
    
