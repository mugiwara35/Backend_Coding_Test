from fastapi_sqlalchemy import db
from sqlalchemy import asc
from datetime import datetime
from schemas.employee_schema import Employee_SchemaCreate, Employee_SchemaUpdate
from models.models import EMPLOYEE
from sqlalchemy.sql import func

def read_employee_all():
    return db.session.query(EMPLOYEE).order_by(asc(EMPLOYEE.id)).all()

def read_employee_byId(id):
    return db.session.query(EMPLOYEE).filter_by(id=id).order_by(asc(EMPLOYEE.id)).first()

def create_employee(schema_employee: Employee_SchemaCreate):    
    db_employee = EMPLOYEE(name=schema_employee.name, phone = schema_employee.phone, wages=schema_employee.wages, role=schema_employee.role)
    db.session.add(db_employee)
    db.session.commit()
    return db_employee

def update_employee(db_employee: EMPLOYEE, schema_employee: Employee_SchemaUpdate):
    db_employee.name = schema_employee.name
    db_employee.phone = schema_employee.phone
    db_employee.wages = schema_employee.wages
    db_employee.role = schema_employee.role
    db_employee.updated_at = func.now()
    
    db.session.commit()
    return db_employee

def delete_employee(db_employee: EMPLOYEE):
    db.session.delete(db_employee)
    db.session.commit()
    return db_employee