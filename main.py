from encuesta import Encuesta, EncuestaLimitadaEdad, EncuestaLimitadaRegion
from usuario import Usuario

## Se definene las alternativas como lista de diccionarios
alternativas_1 = [
    {"contenido": "Sí", "ayuda": "Elige si estás de acuerdo"},
    {"contenido": "No"}
]

alternativas_2 = [
    {"contenido": "Muy satisfecho"},
    {"contenido": "Poco satisfecho"},
    {"contenido": "Nada satisfecho", "ayuda": "Elige si tu experiencia fue mala"}
]

##Se definen las preguntas como lista de diccionarios
preguntas = [
    {"enunciado": "¿Recomendarías el producto?", "requerida": True, "alternativas": alternativas_1, "ayuda": "Sé sincero"},
    {"enunciado": "¿Qué tan satisfecho estás con el servicio?", "requerida": True, "alternativas": alternativas_2}
]

## Se crea una encuesta con restricciones de edad y región
encuesta = EncuestaLimitadaEdad("Encuesta segmentada", preguntas, edad_min=18, edad_max=30)

#Quiero modificar y que los datos sean ingresados por el usuario
correo = input("Ingresa tu correo: ")
edad = int(input("Ingresa tu edad: "))
region = int(input("Ingresa tu región (número): "))

usuario = Usuario(correo, edad, region)

## se muestra la encuesta y preguntas al usuario
print("\nResponde la encuesta:\n")
respuestas = []
for i, pregunta in enumerate(encuesta.preguntas, 1):
    print(f"{i}. {pregunta.enunciado}")
    for j, alt in enumerate(pregunta.alternativas):
        print(f"  [{j}] {alt.mostrar()}")
    respuesta = int(input("Elige una opción (número): "))
    respuestas.append(respuesta)

## El usuario intenta contestar la encuesta
respuestas_anteriores = len(encuesta.respuestas)
usuario.contestar_encuesta(encuesta, respuestas)

## Verificamos si se aceptó o rechazó la respuesta
if len(encuesta.respuestas) > respuestas_anteriores:
    print("\n OK ¡Gracias! Tu respuesta fue registrada.")
else:
    print("\n X Tu respuesta NO fue registrada. Puede que no cumplas con los requisitos de la encuesta.")

## Mostrar resumen
print("\n==== ENCUESTA ====")
print(encuesta.mostrar())

print("\n==== RESPUESTAS ====")
for listado in encuesta.respuestas:
    print(listado.mostrar())