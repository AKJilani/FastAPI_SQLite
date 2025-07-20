from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Item
from app.auth import get_current_user
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic Schemas
class ItemCreate(BaseModel):
    name: str
    description: str

class ItemOut(ItemCreate):
    id: int
    class Config:
        orm_mode = True

# CRUD Endpoints
@router.post("/items/", response_model=ItemOut)
def create_item(item: ItemCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/items/", response_model=List[ItemOut])
def read_items(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Item).all()

@router.get("/items/{item_id}", response_model=ItemOut)
def read_item(item_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/items/{item_id}", response_model=ItemOut)
def update_item(item_id: int, updated: ItemCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item.name = updated.name
    item.description = updated.description
    db.commit()
    db.refresh(item)
    return item

@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"message": "Item deleted"}
