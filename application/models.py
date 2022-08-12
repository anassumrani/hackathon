from application import db


class Customers(db.Model):
    customer_id = db.Column(db.Integer, primary_key =True)
    customer_name = db.Column(db.String(20), nullable = False)
    customer_address = db.Column(db.String(50), nullable = False)
    customer_email = db.Column(db.String(30), nullable = False)
<<<<<<< HEAD
    driver = db.Column(db.I)
=======
    customer_phone_number = db.Column(db.String(11), nullable = False)
  
>>>>>>> a6d2810612fbaf1d452dd82fe76299bcde8c3919
    def __str__(self):
        return f"{self.customer_name},{self.customer_address},{self.customer_email}, {self.customer_phone_number}"


class Drivers(db.Model):
    driver_id = db.Column(db.Integer, primary_key =True)
    driver_name = db.Column(db.String(20), nullable = False)
<<<<<<< HEAD
    Driver_package=db.relationship('Packages', backref='Drivers')
=======
    customer_id = db.Column(db.Integer, db.ForeignKey('Customers.customer_id'),nullable = False)
    
>>>>>>> a6d2810612fbaf1d452dd82fe76299bcde8c3919

class Packages(db.Model): 
    package_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('Customers.customer_id'),nullable = False)
    driver_id = db.Column(db.Integer, db.ForeignKey('Drivers.driver_id') , nullable = False)
    package_barcode = db.Column(db.Integer, nullable = False)
    def __str__(self):
        return f"{self.package_barcode}"