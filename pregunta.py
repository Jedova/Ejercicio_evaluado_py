from alternativa import Alternativa
class Pregunta:
    def __init__(self, enunciado: str, requerida: bool, alternativas: list, ayuda: str = None):
        self._enunciado = enunciado
        self._ayuda = ayuda
        self._requerida = requerida
        ## Se espera que alternativas sea una lista de diccionarios## no se establece la modificación, solo consulta
        self._alternativas = [Alternativa(**a) for a in alternativas]

    ##Getter y Setter para enunciado
    @property
    def enunciado(self):
        return self._enunciado

    @enunciado.setter
    def enunciado(self, nuevo_enunciado):
        self._enunciado = nuevo_enunciado

    ## Getter y Setter para ayuda
    @property
    def ayuda(self):
        return self._ayuda

    @ayuda.setter
    def ayuda(self, nueva_ayuda):
        self._ayuda = nueva_ayuda

    ## etter y Setter para requerida
    @property
    def requerida(self):
        return self._requerida

    @requerida.setter
    def requerida(self, nueva_requerida):
        self._requerida = nueva_requerida

    ## Getter por el momento solo se bsca la lectura para alternativas
    @property
    def alternativas(self):
        return self._alternativas

    ## Método para mostrar la pregunta con todas sus alternativas
    def mostrar(self):
        texto = f"Pregunta: {self._enunciado}"
        if self._ayuda:
            texto += f" (Ayuda: {self._ayuda})"
        texto += "\nAlternativas:"
        for alt in self._alternativas:
            texto += f"\n - {alt.mostrar()}"
        return texto
