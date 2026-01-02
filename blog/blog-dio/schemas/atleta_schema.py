from pydantic import BaseModel

class AtletaCreate(BaseModel):
    nome: str
    idade: int
    categoria: str

class AtletaResponse(AtletaCreate):
    id: int
