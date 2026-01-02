from fastapi import APIRouter
from typing import List
from schemas.atleta_schema import AtletaCreate, AtletaResponse
from services.atleta_service import criar_atleta, listar_atletas

router = APIRouter(
    prefix="/atletas",
    tags=["Atletas"]
)

@router.post("/", response_model=AtletaResponse)
async def criar(atleta: AtletaCreate):
    return await criar_atleta(atleta)

@router.get("/", response_model=List[AtletaResponse])
async def listar():
    return await listar_atletas()
