from typing import List

from typing import Optional

from pydantic import BaseModel

from fastapi import FastAPI, HTTPException

from fastapi.middleware.cors import CORSMiddleware

import alumnes
import aules
import db_alumnat

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class student(BaseModel):
    IdAula: int
    NomAlumne: str
    Cicle: str
    Curs: int 
    Grup: str
    CreatedAt: int
    UpdatedAt: Optional[int] = None

class classroom(BaseModel):
    IdAula: int
    DescAula: str
    Edifici: int
    Pis: int
    CreatedAt: int
    UpdatedAt: int

class ClassroomPartial(BaseModel):
    DescAula: str
    Edifici: int
    Pis: int
    
class studentClassroom(BaseModel):
    IdAula: int
    NomAlumne: str
    Cicle: str
    Curs: int 
    Grup: str
    Aula: ClassroomPartial

class tablaAlumne(BaseModel):
    NomAlumne: str
    Cicle: str
    Curs: int
    Grup: str
    DescAula: str

@app.get("/")
def read_root():
    return {"Students API"}

@app.get("/alumne/list", response_model=List[student])
def read_alumnes():

    pdb = db_alumnat.read_alumne() #Aixó retorna 'alumnes'
    alumnes_sch = alumnes.alumnes_schema(pdb) #Aixó retorna el 'for' declarat a alumnes.py
    return alumnes_sch

@app.get("/alumne/show/{id}", response_model=student)
def read_idAlumne(id): #Com a paràmetre introduim 'id' per que a l'hora de fer les proves al swagger ens ho demani.

    pdb = db_alumnat.read_idAlumne(id)
    alumne_sch = alumnes.alumne_schema(pdb) 

    return alumne_sch


@app.post("/alumne/add")
async def create_student(data: student):
    IdAula = data.IdAula
    NomAlumne = data.NomAlumne
    Cicle = data.Cicle
    Curs = data.Curs
    Grup = data.Grup
    CreatedAt = data.CreatedAt
    l_student_id = db_alumnat.create_student(IdAula,NomAlumne,Cicle,Curs,Grup,CreatedAt)
    return {
        "msg": "S'ha afegit correctament",
        "id alumne": l_student_id,
        "nom": NomAlumne
    }

@app.put("/alumne/update/{id}")
def update_grup(id:int,grup:str):
    updated_records = db_alumnat.update_alumne(id,grup)
    if updated_records == 0:
       raise HTTPException(status_code=404, detail="No hi havia res a actualitzar")
    return {"msg": "S'ha actualitzat correctament", "updated_fields": {"grup": grup}}

@app.delete("/alumne/delete/{id}")
def delete_alumne(id:int):
    deleted_records = db_alumnat.delete_alumne(id)
    if deleted_records == 0:
       raise HTTPException(status_code=404, detail="Items to delete not found")
    return {"msg": "S'ha esborrat correctament"}

@app.get("/alumne/list/all", response_model=List[tablaAlumne])
def read_all_alumnes():
    alumnes_data = db_alumnat.read_all_alumnes()
    
    alumnes_with_aules = [
            {
                "IdAlumne": alumne[0],
                "IdAula": alumne[1],
                "NomAlumne": alumne[2],
                "Cicle": alumne[3],
                "Curs": alumne[4],
                "Grup": alumne[5],
                "Aula": {
                    "DescAula": alumne[6],
                    "Edifici": alumne[7],
                    "Pis": alumne[8],
                }
            }
            for alumne in alumnes_data
        ]
        

    return alumnes_with_aules
