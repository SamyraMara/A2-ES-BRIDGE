"""Canal WhatsApp: classe-base do canal + 3 classes folha (uma por tipo)."""
from notificacoes.base import Notificacao


class NotificacaoWhatsapp(Notificacao):
    def formatar(self, titulo, corpo, urgente):
        return ("*URGENTE* " if urgente else "") + f"*{titulo}*\n{corpo}"

    def transmitir(self, conteudo):
        print(f"[WHATSAPP] para: {self.cliente.telefone}")
        print(conteudo)
        print("-" * 40)


class ConfirmacaoPedidoWhatsapp(NotificacaoWhatsapp):
    def montar_conteudo(self):
        numero = self.dados["numero_pedido"]
        total = f"{self.dados['total']:.2f}".replace(".", ",")
        titulo = f"Pedido {numero} confirmado"
        corpo = f"Recebemos seu pedido {numero} no valor de R$ {total}. Ele já está em separação."
        return titulo, corpo, False


class PagamentoRecusadoWhatsapp(NotificacaoWhatsapp):
    def montar_conteudo(self):
        numero = self.dados["numero_pedido"]
        motivo = self.dados["motivo"]
        titulo = "Pagamento recusado"
        corpo = (f"O pagamento do pedido {numero} foi recusado: {motivo}. "
                 "Atualize a forma de pagamento em até 24 horas para não perder o pedido.")
        return titulo, corpo, True


class PromocaoWhatsapp(NotificacaoWhatsapp):
    def montar_conteudo(self):
        cupom = self.dados["cupom"]
        percentual = self.dados["percentual"]
        validade = self.dados["validade"]
        titulo = f"Só hoje: {percentual}% de desconto em todos os produtos da loja"
        corpo = f"Use o cupom {cupom} até {validade} e aproveite {percentual}% de desconto."
        return titulo, corpo, False