from fastapi import APIRouter

api_router = APIRouter()

# Adicione rotas aqui
@api_router.get("/")
def read_root():
    return {"message": "Olá, mundo!"}