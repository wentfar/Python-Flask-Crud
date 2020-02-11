# coding=UTF-8

from app.models import db, Temperature
from sqlalchemy import desc, cast, DATE, and_
import datetime

class TemperatureDao():
    def saveTemperature(self, employeeId, temperature):

        temperatureObj = Temperature(employeeId=employeeId, temperature=temperature,
                                     createdAt=datetime.datetime.now(),
                                     updatedAt=datetime.datetime.now())
        db.session.add(temperatureObj)
        db.session.commit()
        return "employeeId " + employeeId + " info upload success!"



    def saveOrUpdate(self, employeeId, temperature):
        temperatureObj = Temperature(employeeId=employeeId, temperature=temperature,
                                     createdAt=datetime.datetime.now(),
                                     updatedAt=datetime.datetime.now())

        temperatureOlds = self.queryByEmployeeIdAndDate(employeeId, datetime.datetime.now().date())
        if (temperatureOlds is not None and len(temperatureOlds) != 0 ):
            temperatureOlds[0].temperature = temperature
            db.session.commit()
        else:
            db.session.add(temperatureObj)
            db.session.commit()
        return "employeeId " + employeeId + " info upload success!"



    def list_all(self):
        return Temperature.query.order_by(desc(Temperature.id)).all()



    def queryByEmployeeIdAndDate(self, employeeId, targetDate):

        return db.session.query(Temperature).filter(and_(Temperature.employeeId==employeeId,
                                                         cast(Temperature.createdAt, DATE)==cast(targetDate, DATE))).all()


    def queryByEmployeeId(self, employeeId):
        return db.session.query(Temperature).filter(Temperature.employeeId==employeeId).all()