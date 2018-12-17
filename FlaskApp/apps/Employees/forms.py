from flask_wtf import FlaskForm
from FlaskApp.apps.Employees.models import *
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, Required, ValidationError
from wtforms.fields.html5 import DateField
from flask import request

class EmployeeForm(FlaskForm):
    name = StringField("Tên", validators=[DataRequired()], render_kw={"placeholder": "Nhập tên"})
    address = StringField("Địa chỉ", validators=[DataRequired()], render_kw={"placeholder": "Nhập địa chỉ"} )
    email = StringField("Email", validators=[DataRequired(), Email()], render_kw={"placeholder": "Nhập email"})
    phone = IntegerField("Số điện thoại", validators=[DataRequired()], render_kw={"placeholder": "Nhập số điên thoại"})
    gender = SelectField(
        'Giới tính',
        choices=[('0', 'Nữ'), ('1', 'Nam'), ('2', 'Khác')],
        default=1
    )
    images = FileField("Hình ảnh", validators=[FileAllowed(['ipg', 'png', 'jpeg'])])
    date_of_birth = DateField('Ngày sinh', format = '%Y-%m-%d', description = 'Time that the event will occur')
    submit = SubmitField('Save')

    # def validate_email(self, email):
    #     # if email.data != current_user.email:
    #     a = request.args.get('employee_id')
    #     employee = Employee.query.filter_by(email=email.data).first()
    #     if employee:
    #         raise ValidationError('Email này đã tồn tại.'+ str(a))
