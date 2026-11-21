from notificacoes.canais import CanalEmail, CanalPush, CanalSms, CanalWhatsapp
from notificacoes.notificacao import ConfirmacaoPedido, PagamentoRecusado, Promocao

TIPOS = {
    "confirmacao_pedido": ConfirmacaoPedido,
    "pagamento_recusado": PagamentoRecusado,
    "promocao": Promocao,
}

CANAIS = {
    "email": CanalEmail,
    "sms": CanalSms,
    "push": CanalPush,
    "whatsapp": CanalWhatsapp,
}


def criar_notificacao(tipo, canal, **dados):
    return TIPOS[tipo](CANAIS[canal](), **dados)
