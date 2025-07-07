from listado_respuestas import ListadoRespuestas

class Usuario:
    def __init__(self, correo: str, edad: int, region: int):
        self._correo = correo
        self._edad = edad
        self._region = region

    ##Getter y setter para correo
    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, nuevo_correo):
        self._correo = nuevo_correo

    ##Getter y setter para edad
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

    ##Getter y setter para region
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, nueva_region):
        self._region = nueva_region

    ## Método para contestar una encuesta
    def contestar_encuesta(self, encuesta, respuestas: list[int]):
        listado = ListadoRespuestas(self, respuestas)
        encuesta.agregar_respuestas(listado)
