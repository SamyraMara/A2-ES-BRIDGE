TIPOS = ("confirmacao_pedido", "pagamento_recusado", "promocao")
CANAIS = ("email", "sms", "push", "whatsapp")

DADOS = {
    "confirmacao_pedido": {"numero_pedido": "1001", "total": 349.9},
    "pagamento_recusado": {
        "numero_pedido": "1002",
        "motivo": "o banco emissor não autorizou a transação por suspeita de fraude",
    },
    "promocao": {"cupom": "BLACK25", "percentual": 25, "validade": "30/11/2026"},
}


def executar(classe_cliente, enviar):
    cliente = classe_cliente(
        nome="Ana Souza",
        email="ana.souza@exemplo.com",
        telefone="+55 61 99999-0000",
        push_token="tok-ana-123",
        canal_preferido="whatsapp",
    )
    for tipo in TIPOS:
        for canal in CANAIS:
            print(f"### {tipo} via {canal}")
            enviar(tipo, canal, cliente, **DADOS[tipo])