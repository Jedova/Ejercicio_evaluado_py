from pregunta import Pregunta
from listado_respuestas import ListadoRespuestas

class Encuesta:
    def __init__(self, nombre: str, preguntas: list):
        self._nombre = nombre
        self._preguntas = [Pregunta(**p) for p in preguntas]
        self._respuestas = []

    ## Getter y Setter para nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    ## Getter para respuestas (solo lectura)
    @property
    def respuestas(self):
        return self._respuestas

    ## Getter para preguntas (solo lectura)
    @property
    def preguntas(self):
        return self._preguntas

    def mostrar(self):
        texto = f"Encuesta: {self._nombre}\n"
        for i, pregunta in enumerate(self._preguntas, 1):
            texto += f"\nPregunta {i}:\n{pregunta.mostrar()}"
        return texto

    def agregar_respuestas(self, listado_respuestas: ListadoRespuestas):
        self._respuestas.append(listado_respuestas)


class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre: str, preguntas: list, edad_min: int, edad_max: int):
        super().__init__(nombre, preguntas)
        self._edad_min = edad_min
        self._edad_max = edad_max

    @property
    def edad_min(self):
        return self._edad_min

    @edad_min.setter
    def edad_min(self, nueva_min):
        self._edad_min = nueva_min

    @property
    def edad_max(self):
        return self._edad_max

    @edad_max.setter
    def edad_max(self, nueva_max):
        self._edad_max = nueva_max

    def agregar_respuestas(self, listado_respuestas: ListadoRespuestas):
        edad = listado_respuestas.usuario.edad
        if self._edad_min <= edad <= self._edad_max:
            self._respuestas.append(listado_respuestas)


class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre: str, preguntas: list, regiones: list[int]):
        super().__init__(nombre, preguntas)
        self._regiones = regiones

    @property
    def regiones(self):
        return self._regiones

    @regiones.setter
    def regiones(self, nuevas_regiones):
        self._regiones = nuevas_regiones

    def agregar_respuestas(self, listado_respuestas: ListadoRespuestas):
        region = listado_respuestas.usuario.region
        if region in self._regiones:
            self._respuestas.append(listado_respuestas)
