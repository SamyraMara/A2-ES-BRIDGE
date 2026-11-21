"""Ponto de entrada da versão original (SEM Bridge)."""
import sys

from cenario import executar
from fabrica import criar_notificacao
from notificacoes.base import Cliente


def enviar(tipo, canal, cliente, **dados):
    criar_notificacao(tipo, canal, cliente, **dados).enviar()


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    executar(Cliente, enviar)
