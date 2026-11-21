from abc import ABC, abstractmethod
from notificacoes.mensagem import Mensagem


class Notificacao(ABC):
    def __init__(self, canal, **dados):
        self.canal = canal
        self.dados = dados

    def enviar(self, cliente):
        self.canal.enviar(self.montar(), cliente)

    @abstractmethod
    def montar(self):
        """Retorna a Mensagem (titulo, corpo, urgente) deste tipo."""


class ConfirmacaoPedido(Notificacao):
    def montar(self):
        numero = self.dados["numero_pedido"]
        total = f"{self.dados['total']:.2f}".replace(".", ",")
        titulo = f"Pedido {numero} confirmado"
        corpo = f"Recebemos seu pedido {numero} no valor de R$ {total}. Ele já está em separação."
        return Mensagem(titulo, corpo, False)


class PagamentoRecusado(Notificacao):
    def montar(self):
        numero = self.dados["numero_pedido"]
        motivo = self.dados["motivo"]
        titulo = "Pagamento recusado"
        corpo = (f"O pagamento do pedido {numero} foi recusado: {motivo}. "
                 "Atualize a forma de pagamento em até 24 horas para não perder o pedido.")
        return Mensagem(titulo, corpo, True)


class Promocao(Notificacao):
    def montar(self):
        cupom = self.dados["cupom"]
        percentual = self.dados["percentual"]
        validade = self.dados["validade"]
        titulo = f"Só hoje: {percentual}% de desconto em todos os produtos da loja"
        corpo = f"Use o cupom {cupom} até {validade} e aproveite {percentual}% de desconto."
        return Mensagem(titulo, corpo, False)