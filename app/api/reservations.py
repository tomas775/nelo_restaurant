# app/api/reservations.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from .. import crud, schemas, database
from typing import List
import logging

router = APIRouter()





# Endpoint to create a new reservation
@router.post("/reservations/", response_model=List[schemas.Reservation])
def create_reservation(reservation: schemas.ReservationCreate, db: Session = Depends(database.get_db)):
    try:
        reservations = []
        for diner_id in reservation.diner_ids:
            new_reservation = crud.create_reservation(db, diner_id, reservation.table_id, reservation.time)
            reservations.append(new_reservation)
        return reservations
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to delete a reservation
@router.delete("/reservations/{reservation_id}", response_model=dict)
def delete_reservation(reservation_id: int, db: Session = Depends(database.get_db)):
    crud.delete_reservation(db, reservation_id)
    return {"detail": "Reservation deleted"}

# Endpoint to read all reservations
@router.get("/reservations/", response_model=list[schemas.Reservation])
def read_reservations(db: Session = Depends(database.get_db)):
    return crud.get_all_reservations(db)


    



