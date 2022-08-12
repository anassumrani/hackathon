from flask import request, redirect,url_for, render_template 
from application import app, db
from application.models import *
from application.forms import *

@app.route('/assigned/')
def assigned():
    return 'Drivers Assigned'


@app.route('/assign_driver', methods=['GET','POST'])
def add_driver():
    form = assign_driver_form()
    customer = Customers.query.all()
    form.Customer.choices = [(customer.Customers_id, f"{customer.customer_name} {customer.customer_address} {customer.customer_email}") for customer in Customers]
    if form.validate_on_submit():
        driver = form.driver.data
        customer_id = form.customer.data
        new_assign = Customers(driver=driver,)
        db.session.add(new_assign)
        db.session.commit()
        return redirect (url_for('assigned'))
    else:
        return render_template('manager_form.html', form=form )

@app.route('/')
def Home():
    return render_template('index.html')
     