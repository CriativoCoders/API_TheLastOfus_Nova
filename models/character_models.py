from core.configs import settings
from sqlalchemy import Column, Integer, String

class CharacterModel(settings.DBBaseModel):
    __tablename__ = "characters"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)
    role = Column(String(256), nullable=False)  # Ex: Protagonista, Antagonista, etc.
    personality = Column(String(256), nullable=True)  # Descrição da personalidade
    background = Column(String(256), nullable=True)  # História de fundo do personagem
    image_url = Column(String(256), nullable=True)  # URL da imagem do personagem