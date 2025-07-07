class Alternativa:
    def __init__(self, contenido: str, ayuda: str = None):
        self._contenido = contenido
        self._ayuda = ayuda

    # Getter y Setter para contenido
    @property
    def contenido(self):
        return self._contenido

    @contenido.setter
    def contenido(self, nuevo_contenido):
        self._contenido = nuevo_contenido

    # Getter y Setter para ayuda
    @property
    def ayuda(self):
        return self._ayuda

    @ayuda.setter
    def ayuda(self, nueva_ayuda):
        self._ayuda = nueva_ayuda

    # Método para mostrar la alternativa
    def mostrar(self):
        if self._ayuda:
            return f"Alternativa: {self._contenido} (Ayuda: {self._ayuda})"
        return f"Alternativa: {self._contenido}"
