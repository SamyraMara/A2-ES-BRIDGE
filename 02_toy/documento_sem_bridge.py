'''Toy sem bridge'''
import sys


class RelatorioTexto:
    def renderizar(self, titulo, secoes, conclusoes):
        partes = [f"{titulo.upper()}\n{'=' * len(titulo)}"]
        for t, texto in secoes:
            partes += [f"{t.upper()}\n{'=' * len(t)}", texto]
        return "\n".join(partes + ["Conclusões:"] + [f"* {c}" for c in conclusoes])


class RelatorioMarkdown:
    def renderizar(self, titulo, secoes, conclusoes):
        partes = [f"# {titulo}"]
        for t, texto in secoes:
            partes += [f"# {t}", texto]
        return "\n".join(partes + ["Conclusões:"] + [f"- {c}" for c in conclusoes])


class RelatorioHtml:
    def renderizar(self, titulo, secoes, conclusoes):
        partes = [f"<h1>{titulo}</h1>"]
        for t, texto in secoes:
            partes += [f"<h1>{t}</h1>", f"<p>{texto}</p>"]
        itens = "".join(f"<li>{c}</li>" for c in conclusoes)
        return "\n".join(partes + ["<p>Conclusões:</p>", f"<ul>{itens}</ul>"])


class CartaTexto:
    def renderizar(self, destinatario, paragrafos, remetente):
        saudacao = f"Prezada {destinatario},"
        return "\n".join([f"{saudacao.upper()}\n{'=' * len(saudacao)}", *paragrafos,
                          f"Atenciosamente, {remetente}"])


class CartaMarkdown:
    def renderizar(self, destinatario, paragrafos, remetente):
        return "\n".join([f"# Prezada {destinatario},", *paragrafos, f"Atenciosamente, {remetente}"])


class CartaHtml:
    def renderizar(self, destinatario, paragrafos, remetente):
        corpo = [f"<p>{p}</p>" for p in paragrafos]
        return "\n".join([f"<h1>Prezada {destinatario},</h1>", *corpo,
                          f"<p>Atenciosamente, {remetente}</p>"])


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    rel = ("Vendas 2026", [("Resumo", "Vendas subiram 12%."), ("Riscos", "Estoque baixo.")],
           ["Ampliar estoque", "Manter campanha"])
    carta = ("Maria", ["Obrigado pela visita.", "Até breve."], "João")
    for classe in (RelatorioTexto, RelatorioMarkdown, RelatorioHtml):
        print(f"--- {classe.__name__} ---\n{classe().renderizar(*rel)}")
    for classe in (CartaTexto, CartaMarkdown, CartaHtml):
        print(f"--- {classe.__name__} ---\n{classe().renderizar(*carta)}")