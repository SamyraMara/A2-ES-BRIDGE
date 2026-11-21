from dataclasses import dataclass


@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str
    push_token: str
    canal_preferido: str


@dataclass
class Mensagem:
    titulo: str
    corpo: str
    urgente: bool