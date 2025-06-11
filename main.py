from typing import Optional, List 
from pydantic import BaseModel 
from fastapi import FastAPI, HTTPException

class Mensaje(BaseModel): 
    id: Optional[int] = None 
    user: str 
    mensaje: str

# crear aplicación FASTAPI
app = FastAPI() 

# base de datos simulada
mensajes_db: List[Mensaje] = [] 

#POST:crear mensaje
@app.post("/mensajes", response_model=Mensaje) 
def crear_mensaje(mensaje: Mensaje): 
    mensaje.id = len(mensajes_db) + 1 
    mensajes_db.append(mensaje) 
    return mensaje

#GET:Obtener mensaje por ID
@app.get("/mensajes/{mensaje_id}", response_model=Mensaje) 
def obtener_mensaje(mensaje_id: int): 
    for mensaje in mensajes_db: 
        if mensaje.id == mensaje_id: 
            return mensaje 
    raise HTTPException(status_code=404, detail="Mensaje no encontrado")

# Listar los mensajes
@app.get("/mensajes", response_model=List[Mensaje]) 
def listar_mensajes(): 
    return mensajes_db 
