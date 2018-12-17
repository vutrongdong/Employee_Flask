import os
import secrets
from FlaskApp import app
from PIL import Image
from FlaskApp.apps.Employees.models import *
from FlaskApp.apps.Employees.unils import save_image
from FlaskApp.apps.Employees.forms import EmployeeForm
from flask import render_template, url_for, flash, redirect, request, abort

# index employee
def index():
    employees= Employee.query.all()
    return render_template('Employees/list.html', employees=employees)
# detail employee
def detail(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    return render_template('Employees/detail.html', title="employee.name", employee=employee)
# create employee
def create():
    form = EmployeeForm()
    if form.validate_on_submit():
        flash('Thêm nhân sự thành công!', 'success')
        if form.images.data:
            image_file = save_image(form.images.data)
        else:
            image_file = 'null'
        employee = Employee(
            name = form.name.data,
            address=form.address.data, 
            date_of_birth=form.date_of_birth.data, 
            email=form.email.data, 
            images=image_file, 
            phone=form.phone.data, 
            gender=form.gender.data)
        db.session.add(employee)
        db.session.commit()
        return redirect(url_for('list_employee'))
    return render_template('Employees/form.html', title='New Employee', form=form, lagend="Tạo mới nhân sự")
# update employee
def update(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    form = EmployeeForm()
    if form.validate_on_submit():
        if form.images.data:
            image_file = save_image(form.images.data)
            employee.images = image_file
        employee.name = form.name.data
        employee.address = form.address.data
        employee.email = form.email.data
        employee.phone = form.phone.data
        employee.gender = form.gender.data
        employee.date_of_birth = form.date_of_birth.data
        db.session.commit() 
        flash('Cập nhật nhân sự thành công!', 'success')
        return redirect(url_for('detail_employee', employee_id= employee.id))
    elif request.method =='GET':
        form.name.data = employee.name
        form.address.data = employee.address
        form.email.data = employee.email
        form.phone.data = employee.phone
        form.gender.data = employee.gender
        form.images.data = employee.images
        form.date_of_birth.data = employee.date_of_birth
    return render_template('Employees/form.html', title='Update employee', form=form, lagend="Cập nhật nhân sự")
# delete employee
def delete(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    db.session.delete(employee)
    db.session.commit()
    flash('Xóa nhân sự thành công!', 'success')
    return redirect(url_for('list_employee'))