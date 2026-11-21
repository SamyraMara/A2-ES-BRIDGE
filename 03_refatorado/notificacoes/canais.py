from abc import ABC, abstractmethod

LIMITE_SMS = 160
LIMITE_TITULO_PUSH = 50
LIMITE_CORPO_PUSH = 120

"""Interface dos canais de envio."""
class Canal(ABC):
    @abstractmethod
    def enviar(self, mensagem, cliente):
        """Formata a mensagem segundo as regras do canal e faz o envio simulado."""


def _truncar(texto, limite):
    if len(texto) > limite:
        return texto[:limite - 3] + "..."
    return texto


class CanalEmail(Canal):
    def enviar(self, mensagem, cliente):
        assunto = ("[URGENTE] " if mensagem.urgente else "") + mensagem.titulo
        print(f"[EMAIL] para: {cliente.email}")
        print(f"Assunto: {assunto}")
        print(f"Olá, {cliente.nome}!\n{mensagem.corpo}\n\n-- Equipe LojaX")
        print("-" * 40)


class CanalSms(Canal):
    def enviar(self, mensagem, cliente):
        texto = ("URGENTE: " if mensagem.urgente else "") + f"{mensagem.titulo}: {mensagem.corpo}"
        print(f"[SMS] para: {cliente.telefone}")
        print(_truncar(texto, LIMITE_SMS))
        print("-" * 40)


class CanalPush(Canal):
    def enviar(self, mensagem, cliente):
        titulo = ("(!) " if mensagem.urgente else "") + mensagem.titulo
        print(f"[PUSH] para: {cliente.push_token}")
        print(f"Título: {_truncar(titulo, LIMITE_TITULO_PUSH)}")
        print(f"Corpo: {_truncar(mensagem.corpo, LIMITE_CORPO_PUSH)}")
        print("-" * 40)


class CanalWhatsapp(Canal):
    def enviar(self, mensagem, cliente):
        texto = ("*URGENTE* " if mensagem.urgente else "") + f"*{mensagem.titulo}*\n{mensagem.corpo}"
        print(f"[WHATSAPP] para: {cliente.telefone}")
        print(texto)
        print("-" * 40)