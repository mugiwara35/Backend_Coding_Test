from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import DBSessionMiddleware, db
from sqlalchemy.orm import Session
from fastapi import status

from schemas.employee_schema import Employee_SchemaCreate, Employee_SchemaUpdate, Employee_SchemaId

from crud.employee_crud import read_employee_all, read_employee_byId, create_employee, update_employee, delete_employee
from utils.helpers import success_response, error_response

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter()

@router.get("/employee/list")
async def read_employee_all_route():
    db_employee = read_employee_all()
    if db_employee:
        return success_response(data=db_employee, message="Employee data has been successfully found")
    else:
        raise error_response(message="Employee data not found ", status_code=status.HTTP_404_NOT_FOUND)


@router.post('/employee/create/')
async def create_employee_route(schema_employee: Employee_SchemaCreate):
    db_employee = create_employee(schema_employee)

    if db_employee: 
        data = {
            "id": db_employee.id,
            "name": db_employee.name,
            "phone": db_employee.phone,
            "wages": db_employee.wages,
            "role": db_employee.role,
            "created_at": db_employee.created_at,
            "updated_at": db_employee.updated_at
        }
        return success_response(data=data, message="Employee data has been successfully created", status_code=status.HTTP_201_CREATED)
    else:
        raise error_response(message="Failed to create new employee data ", status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

@router.put('/employee/update/')
async def update_employee_route(schema_employee: Employee_SchemaUpdate):
    db_employee = read_employee_byId(schema_employee.id)

    if db_employee:
        db_employee_update = update_employee(db_employee, schema_employee)
        data = {
            "id": db_employee_update.id,
            "name": db_employee_update.name,
            "phone": db_employee_update.phone,
            "wages": db_employee_update.wages,
            "role": db_employee_update.role,
            "created_at": db_employee_update.created_at,
            "updated_at": db_employee_update.updated_at
        }
        
        return success_response(data=data, message="Employee data has been successfully updated", status_code=status.HTTP_200_OK)
    else:
        raise error_response(message="Data employee not found ", status_code=status.HTTP_404_NOT_FOUND)

@router.delete('/employee/delete/')
async def delete_employee_route(schema_employee: Employee_SchemaId):
    db_employee = read_employee_byId(schema_employee.id)

    if db_employee:
        db_employee_delete = delete_employee(db_employee)
        data = {
            "id": db_employee_delete.id
        }
        return success_response(data=data, message="Employee data has been successfully deleted", status_code=status.HTTP_200_OK)
    else:
        raise error_response(message="Data employee not found ", status_code=status.HTTP_404_NOT_FOUND)