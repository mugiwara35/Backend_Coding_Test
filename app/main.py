import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

from pathlib import Path

from fastapi.middleware.cors import CORSMiddleware


from api.employee_api import router as employee_router


app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url="postgresql://postgres:postgres@127.0.0.1:5432/management")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],  
)

app.include_router(employee_router, tags=["Employee"]) 

if __name__ == '__main__':
    uvicorn.run(f"{Path(__file__).stem}:app", port=8080, host="0.0.0.0", reload=True)