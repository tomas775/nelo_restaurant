
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from .. import crud, schemas, database
from typing import List

router = APIRouter()

# Endpoint to create a new table
@router.post("/tables/", response_model=schemas.Table)
def create_table(table: schemas.TableBase, db: Session = Depends(database.get_db)):
    try:
        return crud.create_table(db, table=table)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to read all tables
@router.get("/tables/", response_model=list[schemas.Table])
def read_tables(db: Session = Depends(database.get_db)):
    return crud.get_all_tables(db)



# Endpoint to update a table
@router.put("/tables/{table_id}", response_model=schemas.Table)
def update_table(table_id: int, table: schemas.TableBase, db: Session = Depends(database.get_db)):
    try:
        return crud.update_table(db, table_id=table_id, table=table)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to delete a table
@router.delete("/tables/{table_id}", response_model=dict)
def delete_table(table_id: int, db: Session = Depends(database.get_db)):
    try:
        crud.delete_table(db, table_id=table_id)
        return {"detail": "Table deleted"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

