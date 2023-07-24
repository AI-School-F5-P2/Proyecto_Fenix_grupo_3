from fastapi import FastAPI
from fastapi.testclient import TestClient
from routers.alumnos_router import alumnos
from routers.clases_router import clases
from routers.packs_router import packs
from routers.inscripciones_router import inscripciones
from routers.profesores_router import profesores
from routers.profesor_clases_router import profesor_clases
from routers.clases_router import clases
from routers.niveles_router import niveles
from decouple import config
from config.db import Base, engine
import uvicorn
#from log import logger

app = FastAPI()
port = config("PORT") 

app.include_router(alumnos)
app.include_router(clases)
app.include_router(niveles)
app.include_router(packs)
app.include_router(profesores)
app.include_router(inscripciones)
app.include_router(profesor_clases)

Base.metadata.create_all(bind=engine)
    

if __name__ == '__main__':
    uvicorn.run("app:app", port=int(port), host='localhost', reload=True)
