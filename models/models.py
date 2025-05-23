from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

class Personagem(Base):
    __tablename__ = "personagens"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False, unique=True)
    descricao = Column(Text)

class Episodio(Base):
    __tablename__ = "episodios"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True, nullable=False, unique=True)
    descricao = Column(Text)
    personagem_id = Column(Integer, ForeignKey('personagens.id'), nullable=False)
    personagem = relationship("Personagem", backref="episodios")