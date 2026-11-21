"""Classes-base da versão original (SEM Bridge): só herança."""
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str
    push_token: str
    canal_preferido: str


class Notificacao(ABC):
    """Esqueleto do envio: montar_conteudo() -> formatar() -> transmitir()."""

    def __init__(self, cliente, **dados):
        self.cliente = cliente
        self.dados = dados

    def enviar(self):
        titulo, corpo, urgente = self.montar_conteudo()
        conteudo = self.formatar(titulo, corpo, urgente)
        self.transmitir(conteudo)

    @abstractmethod
    def montar_conteudo(self):
        """Retorna (titulo, corpo, urgente). Implementado por cada classe folha."""

    @abstractmethod
    def formatar(self, titulo, corpo, urgente):
        """Aplica as regras do canal. Implementado pela classe-base do canal."""

    @abstractmethod
    def transmitir(self, conteudo):
        """Envio simulado (imprime no stdout). Implementado pela classe-base do canal."""
