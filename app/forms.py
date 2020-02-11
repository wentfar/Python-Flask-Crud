# coding=UTF-8

from wtforms import Form, StringField, FloatField, SubmitField, DateField, validators, simple, widgets
import datetime
from wtforms.fields.html5 import DateField


class NewTempForm(Form):
    employeeId = StringField(label=u'员工编号',
                             validators=[
                                 validators.DataRequired(message=u'员工编号不能为空'),
                                 validators.regexp('\d{6}', message=u'必须为6位数字'),
                                 validators.Length(min=6, max=6, message=u'员工编号长度必须为%(min)d')],
                             widget=widgets.TextInput(),
                             render_kw={'class': 'text'}
                             )
    temperature = FloatField(label=u'体温',
                             validators=[
                                 validators.DataRequired(message=u'体温格式不正确')],
                             widget=widgets.TextInput(),
                             render_kw={'class': 'text'}
                             )
    submit = SubmitField('save')


class GetForm(Form):
    employeeId = StringField(label=u'员工编号',
                             validators=[
                                 validators.DataRequired(message=u'员工编号不能为空'),
                                 validators.regexp('\d{6}', message=u'必须为6位数字'),
                                 validators.Length(min=6, max=6, message=u'员工编号长度必须为%(min)d')],
                             widget=widgets.TextInput(),
                             render_kw={'class': 'text'}
                             )

    recordDate = DateField(label=u'日期',
                           validators=[validators.InputRequired(message=u'日期不能为空')],
                           format='%Y-%m-%d',
                           default=datetime.datetime.today(),
                           render_kw={'class': 'datepicker'})

    submit = SubmitField('get')
