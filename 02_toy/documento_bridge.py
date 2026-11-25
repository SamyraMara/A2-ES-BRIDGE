"""Padrão Bridge em miniatura: Documento (abstração) x Formato (implementação).

"""
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
