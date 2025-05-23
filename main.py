from fastapi import FastAPI, Request, HTTPException
from core.configs import settings
from fastapi.middleware.cors import CORSMiddleware
from api.v1.api import api_router
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="API de The Last of Us - DS 15",
    description="API para gerenciar dados de The Last of Us",
    version="1.0.0"
)

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)

class Personagem(BaseModel):
    nome: str
    imagem_url: Optional[str] = None
    descricao: Optional[str] = None

personagens = [{"id": 1, "nome": "Joel", "descricao": "Protagonista do jogo"}]

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/personagens")
def ler_personagens():
    return personagens

@app.get("/personagens/{personagem_id}")
def ler_personagem(personagem_id: int):
    for p in personagens:
        if p["id"] == personagem_id:
            return p
    raise HTTPException(status_code=404, detail="Personagem não encontrado")

@app.post("/personagens")
def criar_personagem(personagem: Personagem):
    personagem_dict = personagem.dict()
    novo_personagem = {
        "id": len(personagens) + 1,
        "nome": personagem_dict["nome"],
        "imagem_url": personagem_dict["imagem_url"],
        "descricao": personagem_dict["descricao"]
    }
    personagens.append(novo_personagem)
    return {"message": "Personagem criado com sucesso"}

@app.put("/personagens/{personagem_id}")
def atualizar_personagem(personagem_id: int, personagem: Personagem):
    personagem_dict = personagem.dict()
    for p in personagens:
        if p["id"] == personagem_id:
            p["nome"] = personagem_dict["nome"]
            p["imagem_url"] = personagem_dict["imagem_url"]
            p["descricao"] = personagem_dict["descricao"]
            return {"message": "Personagem atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Personagem não encontrado")

@app.delete("/personagens/{personagem_id}")
def deletar_personagem(personagem_id: int):
    for p in personagens:
        if p["id"] == personagem_id:
            personagens.remove(p)
            return {"message": "Personagem deletado com sucesso"}
    raise HTTPException(status_code=404, detail="Personagem não encontrado")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        log_level="info",
        reload=True,
        debug=True
    )