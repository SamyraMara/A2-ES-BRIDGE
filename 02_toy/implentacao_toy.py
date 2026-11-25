"""Demonstrações e testes do toy Bridge (o núcleo do padrão está em documento_bridge.py)."""
import sys

from documento_bridge import Carta, Formato, HtmlSimples, Markdown, Relatorio, TextoPuro


class FormatoBBCode(Formato):
    def titulo(self, texto): return f"[b]{texto}[/b]"
    def paragrafo(self, texto): return texto
    def lista(self, itens): return "[list]" + "".join(f"[*]{i}" for i in itens) + "[/list]"

class FormatoFalso(Formato):
    def __init__(self): self.chamadas = []
    def titulo(self, texto): self.chamadas.append(("titulo", texto)); return ""
    def paragrafo(self, texto): self.chamadas.append(("paragrafo", texto)); return ""
    def lista(self, itens): self.chamadas.append(("lista", list(itens))); return ""


DADOS_RELATORIO = ("Vendas 2026",
                   [("Resumo", "Vendas subiram 12%."), ("Riscos", "Estoque baixo.")],
                   ["Ampliar estoque", "Manter campanha"])
DADOS_CARTA = ("Maria", ["Obrigado pela visita.", "Até breve."], "João")


def demo_formatos():
    """1. Cada abstração com cada implementador: 6 saídas a partir de 5 classes concretas."""
    print("== 1. Mesmo documento nos 3 formatos ==")
    for classe, dados in ((Relatorio, DADOS_RELATORIO), (Carta, DADOS_CARTA)):
        for formato in (TextoPuro(), Markdown(), HtmlSimples()):
            print(f"--- {classe.__name__} / {type(formato).__name__} ---")
            print(classe(formato, *dados).renderizar())


def demo_troca_runtime():
    """2. Como a ponte é um atributo, o implementador do mesmo objeto pode ser trocado."""
    print("\n== 2. Troca de formato em runtime ==")
    documento = Carta(Markdown(), *DADOS_CARTA)
    print(documento.renderizar())
    documento.formato = HtmlSimples()
    print(documento.renderizar())


def demo_extensao_bbcode():
    """3. Um formato novo funciona com todos os documentos que já existem."""
    print("\n== 3. Extensão: novo formato sem alterar classes existentes ==")
    print(Relatorio(FormatoBBCode(), *DADOS_RELATORIO).renderizar())
    print(Carta(FormatoBBCode(), *DADOS_CARTA).renderizar())


def demo_formato_falso():
    """4. A abstração pode ser testada isoladamente com um implementador falso."""
    print("\n== 4. Teste com FormatoFalso (sem gerar texto real) ==")
    falso = FormatoFalso()
    Relatorio(falso, *DADOS_RELATORIO).renderizar()
    print("\n".join(str(c) for c in falso.chamadas))
    assert falso.chamadas[0] == ("titulo", "Vendas 2026") and falso.chamadas[-1][0] == "lista"
    print("OK: Relatorio chamou titulo/paragrafo/lista na ordem esperada.")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    demo_formatos()
    demo_troca_runtime()
    demo_extensao_bbcode()
    demo_formato_falso()

if __name__ == "__main__":
    main()
