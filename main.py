from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()
@app.get("/")
def home():
    return {"msg": "Enterprise IT Service Desk -Server "}

db = {
    1: {"ID" : 1,"Title": "Computer is not on" ,
         "description": "Power button is not working", 
         "Category": "Hardware", "Status": "New"},
    2: {"ID" : 2, "Title":"Internet is not on" , 
         "description": "WIFI PROBLEM", 
         "Category": "Hardware", "Status": "New"} 
}
#Schemas 
class TicketCreate(BaseModel):
    title : str
    description : str
    Category : str
    status : str

class TicketResponse(TicketCreate):
    id : int
#APIs
@app.get("/tickets")
def ticket_read_all():
    return list(db.values())

@app.get("/tickets/{id}")
def ticket_read_by_id(id: int):
    if id not in db:
        raise  HTTPException(detail="Ticket not found", status_code=404)
    return db[id]

@app.post("/tickets", status_code=201, response_model=TicketResponse)
def ticket_create(ticket_payload : TicketCreate):
    new_id = max(db.keys(), default=0) +1
    db[new_id]={"id" : new_id, **ticket_payload.model_dump()}
    return db[new_id]

@app.put("/tickets/{id}", response_model=TicketResponse)
def tickets_update(id : int, payload : TicketCreate):
    if id not in db:
        raise HTTPException(detail="Ticket Not Found", status_code=404)
    db[id]={"id" : id, **payload.model_dump()}
    return db[ib]
@app.delete("/ticket {id}")
def tickets_delete(id: int):
    if id not in db:
        raise HTTPException(detail="Ticket not found",status_code=404)
    del db[id]
    return {"Message":"Ticket deleted successfully"}
    
@app.get("/tickets/{id}")
def ticket_read_by_id(id: int):
    if id not in db:
        raise  HTTPException(detail="Ticket not found", status_code=404)
    del db[id]
    return {"Message" : "Ticket Deleted Successfully"}