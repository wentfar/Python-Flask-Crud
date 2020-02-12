# coding=UTF-8

from wtforms import Form, StringField, FloatField, SubmitField, DateField, validators, simple, widgets
import datetime
from wtforms.fields.html5 import DateField


class NewForm(Form):
    employeeId = StringField(label=u'员工编号',
                             validators=[
                                 validators.DataRequired(message=u'员工编号不能为空'),
                                 validators.regexp('\d{6}', message=u'必须为6位数字'),
                                 validators.Length(min=6, max=6, message=u'员工编号长度必须为%(min)d')],
                             widget=widgets.TextInput(),
                             render_kw={'class': 'form-control'}
                             )
    temperature = FloatField(label=u'体温',
                             validators=[
                                 validators.DataRequired(message=u'体温格式不正确')],
                             widget=widgets.TextInput(),
                             render_kw={'class': 'form-control'}
                             )
    new = SubmitField(render_kw='btn btn-success')


class QueryForm(Form):
    employeeId = StringField(label=u'员工编号',
                             validators=[
                                 validators.DataRequired(message=u'员工编号不能为空'),
                                 validators.regexp('\d{6}', message=u'必须为6位数字'),
                                 validators.Length(min=6, max=6, message=u'员工编号长度必须为%(min)d')],
                             widget=widgets.TextInput(),
                             render_kw={'class': 'form-control'}
                             )

    recordDate = DateField(label=u'日期',
                           validators=[validators.InputRequired(message=u'日期不能为空')],
                           format='%Y-%m-%d',
                           default=datetime.datetime.today(),
                           render_kw={'class': 'datepicker'})

    query = SubmitField(render_kw='btn btn-success')