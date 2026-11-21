"""Ponto de entrada da versão refatorada (COM Bridge)."""
import sys

from cenario import executar
from notificacoes.mensagem import Cliente
from registro import criar_notificacao


def enviar(tipo, canal, cliente, **dados):
    criar_notificacao(tipo, canal, **dados).enviar(cliente)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    executar(Cliente, enviar)
