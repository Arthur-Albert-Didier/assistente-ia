from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from app.memory.database import Base


class Conversa(Base):
    """Histórico de todas as mensagens trocadas."""
    __tablename__ = "conversas"

    id         = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, nullable=False)
    mensagem   = Column(Text, nullable=False)
    resposta   = Column(Text, nullable=False)
    criado_em  = Column(DateTime, server_default=func.now())


class Atividade(Base):
    """Registro de atividades como estudo, corrida e treino."""
    __tablename__ = "atividades"

    id         = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, nullable=False)
    tipo       = Column(String(50), nullable=False)   # estudo | corrida | treino
    duracao    = Column(Integer, nullable=True)        # em minutos
    descricao  = Column(Text, nullable=True)
    criado_em  = Column(DateTime, server_default=func.now())


class Lembrete(Base):
    """Lembretes criados pelo usuário."""
    __tablename__ = "lembretes"

    id         = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, nullable=False)
    texto      = Column(Text, nullable=False)
    agendado   = Column(DateTime, nullable=True)
    concluido  = Column(Integer, default=0)            # 0 = pendente, 1 = concluído
    criado_em  = Column(DateTime, server_default=func.now())
