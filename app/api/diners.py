
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from .. import crud, schemas, database
from typing import List

router = APIRouter()

# Endpoint to read all diners
@router.get("/diners/", response_model=list[schemas.Diner])
def read_diners(db: Session = Depends(database.get_db)):
    return crud.get_all_diners(db)


# Endpoint to create a new diner
@router.post("/diners/", response_model=schemas.Diner)
def create_diner(diner: schemas.DinerCreate, db: Session = Depends(database.get_db)):
    try:
        return crud.create_diner(db, name=diner.name, dietary_restrictions=diner.dietary_restrictions)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
