from pregunta import Pregunta
from alternativa import Alternativa

if __name__ == "__main__":
    alternativas = [
        {"contenido": "Sí", "ayuda": "Marca si estás de acuerdo"},
        {"contenido": "No"},
        {"contenido": "No sabe / No responde", "ayuda": "Opción neutral"}
    ]

    pregunta = Pregunta("¿Está satisfecho con el servicio?", True, alternativas, "Responde honestamente")

    print(pregunta.mostrar())
