from usuario import Usuario

class ListadoRespuestas:
    def __init__(self, usuario: Usuario, respuestas: list[int]):
        self._usuario = usuario
        self._respuestas = respuestas

    @property
    def usuario(self):
        return self._usuario

    @property
    def respuestas(self):
        return self._respuestas

    def mostrar(self):
        texto = f"Usuario: {self._usuario.correo} respondió: {self._respuestas}"
        return texto
