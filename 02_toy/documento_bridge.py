"""Padrão Bridge em miniatura: Documento (abstração) x Formato (implementação)."""
import sys
from abc import ABC, abstractmethod

class Formato(ABC):
    @abstractmethod
    def titulo(self, texto): ...
    @abstractmethod
    def paragrafo(self, texto): ...
    @abstractmethod
    def lista(self, itens): ...

class TextoPuro(Formato):
    def titulo(self, texto): return f"{texto.upper()}\n{'=' * len(texto)}"
    def paragrafo(self, texto): return texto
    def lista(self, itens): return "\n".join(f"* {i}" for i in itens)

class Markdown(Formato):
    def titulo(self, texto): return f"# {texto}"
    def paragrafo(self, texto): return texto
    def lista(self, itens): return "\n".join(f"- {i}" for i in itens)

class HtmlSimples(Formato):
    def titulo(self, texto): return f"<h1>{texto}</h1>"
    def paragrafo(self, texto): return f"<p>{texto}</p>"
    def lista(self, itens): return "<ul>" + "".join(f"<li>{i}</li>" for i in itens) + "</ul>"

class Documento(ABC):
    def __init__(self, formato):
        self.formato = formato
    @abstractmethod
    def renderizar(self): ...

class Relatorio(Documento):
    def __init__(self, formato, titulo, secoes, conclusoes):
        super().__init__(formato)
        self.titulo, self.secoes, self.conclusoes = titulo, secoes, conclusoes
    def renderizar(self):
        f = self.formato
        partes = [f.titulo(self.titulo)]
        for titulo, texto in self.secoes:
            partes += [f.titulo(titulo), f.paragrafo(texto)]
        partes += [f.paragrafo("Conclusões:"), f.lista(self.conclusoes)]
        return "\n".join(partes)

class Carta(Documento):
    def __init__(self, formato, destinatario, paragrafos, remetente):
        super().__init__(formato)
        self.destinatario, self.paragrafos, self.remetente = destinatario, paragrafos, remetente
    def renderizar(self):
        f = self.formato
        partes = [f.titulo(f"Prezada {self.destinatario},")]
        partes += [f.paragrafo(p) for p in self.paragrafos]
        partes.append(f.paragrafo(f"Atenciosamente, {self.remetente}"))
        return "\n".join(partes)

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    dados_rel = ("Vendas 2026", [("Resumo", "Vendas subiram 12%."), ("Riscos", "Estoque baixo.")],
                 ["Ampliar estoque", "Manter campanha"])
    dados_carta = ("Maria", ["Obrigado pela visita.", "Até breve."], "João")
    print("== 1. Mesmo documento nos 3 formatos ==")
    for classe, dados in ((Relatorio, dados_rel), (Carta, dados_carta)):
        for fmt in (TextoPuro(), Markdown(), HtmlSimples()):
            print(f"--- {classe.__name__} / {type(fmt).__name__} ---")
            print(classe(fmt, *dados).renderizar())
            
    print("\n== 2. Troca de formato em runtime ==")
    documento = Carta(Markdown(), *dados_carta)
    print(documento.renderizar())
    documento.formato = HtmlSimples()
    print(documento.renderizar())
    
    print("\n== 3. Extensão: novo formato sem alterar classes existentes ==")
    class FormatoBBCode(Formato):
        def titulo(self, texto): return f"[b]{texto}[/b]"
        def paragrafo(self, texto): return texto
        def lista(self, itens): return "[list]" + "".join(f"[*]{i}" for i in itens) + "[/list]"
    print(Relatorio(FormatoBBCode(), *dados_rel).renderizar())
    print(Carta(FormatoBBCode(), *dados_carta).renderizar())
    
    print("\n== 4. Teste com FormatoFalso (sem gerar texto real) ==")
    class FormatoFalso(Formato):
        def __init__(self): self.chamadas = []
        def titulo(self, texto): self.chamadas.append(("titulo", texto)); return ""
        def paragrafo(self, texto): self.chamadas.append(("paragrafo", texto)); return ""
        def lista(self, itens): self.chamadas.append(("lista", list(itens))); return ""
    falso = FormatoFalso()
    Relatorio(falso, *dados_rel).renderizar()
    print("\n".join(str(c) for c in falso.chamadas))
    assert falso.chamadas[0] == ("titulo", "Vendas 2026") and falso.chamadas[-1][0] == "lista"
    print("OK: Relatorio chamou titulo/paragrafo/lista na ordem esperada.")
