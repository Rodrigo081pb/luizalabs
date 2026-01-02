from models.atleta_model import Atleta

# Banco de dados em memória (lista)
atletas_db = []

async def criar_atleta(atleta):
    novo_atleta = Atleta(
        id=len(atletas_db) + 1,
        nome=atleta.nome,
        idade=atleta.idade,
        categoria=atleta.categoria
    )
    atletas_db.append(novo_atleta)

    return {
        "id": novo_atleta.id,
        "nome": novo_atleta.nome,
        "idade": novo_atleta.idade,
        "categoria": novo_atleta.categoria
    }

async def listar_atletas():
    return [
        {
            "id": a.id,
            "nome": a.nome,
            "idade": a.idade,
            "categoria": a.categoria
        }
        for a in atletas_db
    ]
