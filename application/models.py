from application import db 

class Customers(db.Model):
    customer_id = db.Column(db.Integer, primary_key =True)
    customer_name = db.Column(db.String(20), nullabe = False)
    customer_address = db.Column(db.String(50), nullable = False)
    customer_email = db.Column(db.String(30), nullable = False)
    driver = db.Column(db.I)
    def __str__(self):
        return f"{self.customer_name},{self.customer_address},{self.customer_email}"


class Drivers(db.Model):
    driver_id = db.Column(db.Integer, primary_key =True)
    driver_name = db.Column(db.String(20), nullable = False)
    Driver_package=db.relationship('Packages', backref='Drivers')

class Packages(db.Model): 
    package_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('Customers.customer_id'),nullable = False)
    driver_id = db.Column(db.Integer, db.ForeignKey('Drivers.driver_id') , nullable = False)
    package_barcode = db.Column(db.Integer, nullable = False)
    def __str__(self):
        return f"{self.package_barcode}"