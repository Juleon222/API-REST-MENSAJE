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

