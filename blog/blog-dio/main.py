from fastapi import FastAPI
from controllers.atleta_controller import router as atleta_router

app = FastAPI(
    title="API CrossFit",
    description="API assíncrona para academia e competição de CrossFit",
    version="1.0.0"
)

app.include_router(atleta_router)

@app.get("/")
async def home():
    return {"mensagem": "API CrossFit rodando com sucesso!"}
