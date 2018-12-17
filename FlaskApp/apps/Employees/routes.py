from flask import render_template
from FlaskApp import app
from FlaskApp.apps.Employees import controller

# list employee
@app.route("/employee")
def list_employee():
    return controller.index()

# detail employee
@app.route("/employee/<int:employee_id>")
def detail_employee(employee_id):
    return controller.detail(employee_id)

# create employee
@app.route("/employee/new", methods=['GET', 'POST'])
def new_employee():
    return controller.create()

# update employee
@app.route("/employee/<int:employee_id>/update", methods=['GET', 'POST'])
def update_employee(employee_id):
    return controller.update(employee_id)

# delete employee
@app.route("/employee/<int:employee_id>/delete", methods=['GET', 'POST'])
def delete_employee(employee_id):
    return controller.delete(employee_id)
