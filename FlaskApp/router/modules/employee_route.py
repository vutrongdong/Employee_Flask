from flask import render_template
from FlaskApp import app
from FlaskApp.apps.Controllers import EmployeeController

# list employee
@app.route("/employee")
def list_employee():
    return EmployeeController.index()

# detail employee
@app.route("/employee/<int:employee_id>")
def detail_employee(employee_id):
    return EmployeeController.detail(employee_id)

# create employee
@app.route("/employee/new", methods=['GET', 'POST'])
def new_employee():
    return EmployeeController.create()

# update employee
@app.route("/employee/<int:employee_id>/update", methods=['GET', 'POST'])
def update_employee(employee_id):
    return EmployeeController.update(employee_id)


# delete employee
@app.route("/employee/<int:employee_id>/delete", methods=['GET', 'POST'])
def delete_employee(employee_id):
    return EmployeeController.delete(employee_id)
