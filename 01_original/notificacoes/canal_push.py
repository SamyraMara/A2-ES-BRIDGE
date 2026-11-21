"""Canal push: classe-base do canal + 3 classes folha (uma por tipo)."""
from notificacoes.base import Notificacao

LIMITE_TITULO_PUSH = 50
LIMITE_CORPO_PUSH = 120


class NotificacaoPush(Notificacao):
    @staticmethod
    def _truncar(texto, limite):
        if len(texto) > limite:
            return texto[:limite - 3] + "..."
        return texto

    def formatar(self, titulo, corpo, urgente):
        titulo = ("(!) " if urgente else "") + titulo
        return (self._truncar(titulo, LIMITE_TITULO_PUSH),
                self._truncar(corpo, LIMITE_CORPO_PUSH))

    def transmitir(self, conteudo):
        titulo, corpo = conteudo
        print(f"[PUSH] para: {self.cliente.push_token}")
        print(f"Título: {titulo}")
        print(f"Corpo: {corpo}")
        print("-" * 40)


class ConfirmacaoPedidoPush(NotificacaoPush):
    def montar_conteudo(self):
        numero = self.dados["numero_pedido"]
        total = f"{self.dados['total']:.2f}".replace(".", ",")
        titulo = f"Pedido {numero} confirmado"
        corpo = f"Recebemos seu pedido {numero} no valor de R$ {total}. Ele já está em separação."
        return titulo, corpo, False


class PagamentoRecusadoPush(NotificacaoPush):
    def montar_conteudo(self):
        numero = self.dados["numero_pedido"]
        motivo = self.dados["motivo"]
        titulo = "Pagamento recusado"
        corpo = (f"O pagamento do pedido {numero} foi recusado: {motivo}. "
                 "Atualize a forma de pagamento em até 24 horas para não perder o pedido.")
        return titulo, corpo, True


class PromocaoPush(NotificacaoPush):
    def montar_conteudo(self):
        cupom = self.dados["cupom"]
        percentual = self.dados["percentual"]
        validade = self.dados["validade"]
        titulo = f"Só hoje: {percentual}% de desconto em todos os produtos da loja"
        corpo = f"Use o cupom {cupom} até {validade} e aproveite {percentual}% de desconto."
        return titulo, corpo, False