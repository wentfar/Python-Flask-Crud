from flask import request, render_template, Blueprint, flash, redirect, url_for
from app.services import TemperatureDao
from app.forms import *
from app.utils import datetime2date
import datetime

tempBp = Blueprint('TempBp', __name__, template_folder='templates')


@tempBp.route('/index')
# @tempBp.route('/')
def index():
    temperatureDao = TemperatureDao()
    temperatures = temperatureDao.list_all()
    return render_template('index.html', temperatures=temperatures)


@tempBp.route('/query', methods=['GET', 'POST'])
def query():
    if request.method == 'GET':
        form = QueryForm()
        return render_template('query.html', form=form)

    if request.method == 'POST':
        form = QueryForm(formdata=request.form)
        if form.validate():
            employeeId = form.data['employeeId']
            recordDate = form.data['recordDate']

            temperatureDao = TemperatureDao()
            temperatures = temperatureDao.queryByEmployeeIdAndDate(employeeId, recordDate)
            if (temperatures is None):
                temperatures = []
            return render_template('index.html', temperatures=temperatures)
        else:
            return render_template('query.html', form=form)


@tempBp.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'GET':
        form = NewForm()
        return render_template('new.html', form=form)

    if request.method == 'POST':
        form = NewForm(formdata=request.form)
        if form.validate():

            employeeId = form.data['employeeId']
            temperature = form.data['temperature']

            temperatureDao = TemperatureDao()
            message = temperatureDao.saveOrUpdate(employeeId, temperature)

            return redirect(url_for('TempBp.index'))
        else:
            return render_template('new.html', form=form)
