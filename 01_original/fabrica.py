from notificacoes.canal_email import (ConfirmacaoPedidoEmail, PagamentoRecusadoEmail, PromocaoEmail)
from notificacoes.canal_push import (ConfirmacaoPedidoPush, PagamentoRecusadoPush, PromocaoPush)
from notificacoes.canal_sms import ConfirmacaoPedidoSms, PagamentoRecusadoSms, PromocaoSms
from notificacoes.canal_whatsapp import (ConfirmacaoPedidoWhatsapp, PagamentoRecusadoWhatsapp, PromocaoWhatsapp)


def criar_notificacao(tipo, canal, cliente, **dados):
    if tipo == "confirmacao_pedido" and canal == "email":
        return ConfirmacaoPedidoEmail(cliente, **dados)
    elif tipo == "confirmacao_pedido" and canal == "sms":
        return ConfirmacaoPedidoSms(cliente, **dados)
    elif tipo == "confirmacao_pedido" and canal == "push":
        return ConfirmacaoPedidoPush(cliente, **dados)
    elif tipo == "confirmacao_pedido" and canal == "whatsapp":
        return ConfirmacaoPedidoWhatsapp(cliente, **dados)
    elif tipo == "pagamento_recusado" and canal == "email":
        return PagamentoRecusadoEmail(cliente, **dados)
    elif tipo == "pagamento_recusado" and canal == "sms":
        return PagamentoRecusadoSms(cliente, **dados)
    elif tipo == "pagamento_recusado" and canal == "push":
        return PagamentoRecusadoPush(cliente, **dados)
    elif tipo == "pagamento_recusado" and canal == "whatsapp":
        return PagamentoRecusadoWhatsapp(cliente, **dados)
    elif tipo == "promocao" and canal == "email":
        return PromocaoEmail(cliente, **dados)
    elif tipo == "promocao" and canal == "sms":
        return PromocaoSms(cliente, **dados)
    elif tipo == "promocao" and canal == "push":
        return PromocaoPush(cliente, **dados)
    elif tipo == "promocao" and canal == "whatsapp":
        return PromocaoWhatsapp(cliente, **dados)
    else:
        raise ValueError(f"Combinação desconhecida: {tipo} / {canal}")
