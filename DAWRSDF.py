import random

# Mediante diccionarios agregar cada pregunta con su respuesta 
preguntas = {
    "ciencia": [ 
        {
            "pregunta": "Una integral definida se puede solucionar solo si:",
            "respuestas": ["A- Tiene unicamente una variable", "B- es continua en su intervalo definido", "C- Se realiza unicamente con respecto al eje X", "D- ninguna de las anteriores"],
            "respuesta correcta": "B"
        },
        {
            "pregunta": "¿Que es la fotosintesis?:",
            "respuestas": ["A- El sistema nervioso de las plantas", "B- La interaccion nutricional de las plantas con su entorno", "C- Un mecanismo de defensa de las plantas", "D- La conversion de materia inorganica a organica en las plantas"],
            "respuesta correcta": "D"
        },
        {
            "pregunta": "El autor de la relatividad es: ",
            "respuestas": ["A- Artur schoppenhauer", "B- Isaac Newton", "C- Albert Einstein", "D- Maxwell"],
            "respuesta correcta": "C"
        },
        {
            "pregunta": "¿Quien fue el autor del desarrollo de la bomba atomica?",
            "respuestas": ["A- Schrodingger", "B- Albert Einstein", "C- Robert Oppenheimer", "D- Marie Curie"],
            "respuesta correcta": "C"
        },
        {
            "pregunta": "¿Que es un poliedro?",
            "respuestas": ["A- Una figura geometrica en 2 D", "B- Un solido con volumen infinito", "C- Un solido irregular", "D- Un solido con caras planas"],
            "respuesta correcta": "D"
        },
        {
            "pregunta": "¿De que se compone el agua?:?",
            "respuestas": ["A- Calcio", "B- Hidrogeno y Oxigeno", "C- Sodio y Oxigeno", "D- Mercurio e hidrogeno"],
            "respuesta correcta": "B"
        },
        {
            "pregunta": "¿el principio de incertidumbre parte de:?",
            "respuestas": ["A- No saber nada con certeza", "B- Interpretar un dato cuantico de manera imprecisa", "C- El conocimiento es finito", "D- No poder conocer datos cuanticos a la vez de forma precisa"],
            "respuesta correcta": "D"
        },
        {
            "pregunta": "¿Quien invento las computadoras?:",
            "respuestas": ["A- Mark zuckerberg", "B- Steve Jobs", "C- Charles Babbage", "D- Angel Albeiro Ricardo"],
            "respuesta correcta": "C"
        },
        {
            "pregunta": "¿Un vector se compone de:?",
            "respuestas": ["A- Masa y densidad", "B- Angulo y fase", "C- Direccion y magnitud", "D- Velocidad angular y sentido"],
            "respuesta correcta": "C"
        },
        {
            "pregunta": "¿cuantos huesos tiene la mano humana?: ",
            "respuestas": ["A- 27", "B- 14", "C- 15", "D- 28"],
            "respuesta correcta": "A"
        }        
    ],
    "Deportes": [ 
        {
            "pregunta": "Cuál es el deporte más popular del mundo",
            "respuestas": ["A-Baloncesto", "B- futbol", "C- voleyball", "D- tenis"],
            "respuesta correcta": "B"
        },
        {
            "pregunta": "¿Qué país ganó el mundial de Fútbol en 2018?",
            "respuestas": ["A- Francia", "B- Argentina", "C- Alemania", "D- Colombia"],
            "respuesta correcta": "A"
        },
        {
            "pregunta": "¿Qué evento deportivo se celebra cada cuatro años y reúne a atletas de todo el mundo?",
            "respuestas": ["A- Mundial", "B- Olimpicos", "C- Copa America ", "D- tour de Francia"],
            "respuesta correcta": "B"
        },
        {
            "pregunta": "¿Cuál es el equipo de béisbol más famoso de Nueva York?",
            "respuestas": ["A- Meets", "B- Yankees", "C- Red sox", "D- Tolima"],
            "respuesta correcta": "B"
        },
        {
            "pregunta": "¿Quien es mejor ¿Cristiano o messi??",
            "respuestas": ["A- Messi", "B- Messi sin duda", "C- CR6 ", "D- Dairo Moreno"],
            "respuesta correcta": "D"
        },
        {
            "pregunta": "¿Cuantos colores tiene la bandera de los Olimpicos?",
            "respuestas": ["A- 4", "B- 5", "C- 6", "D- no tiene bandera"],
            "respuesta correcta": "B"
        },
        {
            "pregunta": "¿Quién es conocido como el rey del fútbol?",
            "respuestas": ["A- Messi", "B- Pele", "C- Maradona", "D- Angel (el kaiser)"],
            "respuesta correcta": "D"
        },
        {
            "pregunta": "¿En qué deporte se utilizan las palabras ace y deuce?",
            "respuestas": ["A- Beisbol", "B- Baloncesto", "C- Tenis", "D- Pool"],
            "respuesta correcta": "C"
        },
        {
            "pregunta": "¿En qué deporte se utiliza un disco volador?",
            "respuestas": ["A-Rugby ", "B- tiro con arco", "C- Ultimate frisbee", "D- Hockey"],
            "respuesta correcta": "C"
        },
        {
            "pregunta": "¿Millonarios es?",
            "respuestas": ["A- El mejor equipo de colombia", "B- Mejor que nacional", "C- Los GOATS", "D- Todas las anteriores"],
            "respuesta correcta": "D"
        }
    ]
}

# Funcion para revisar si se acabaron las preguntas
def Revision_preguntas(preguntas, categoria):
    
    if not preguntas[categoria]:
        del preguntas[categoria]
    
    print("¡No hay más preguntas disponibles!")    

# Funcion para desplegar las preguntas
def Mis_Preguntas(diccionario):
    
        categoria = random.choice(list(preguntas.keys()))
        print(f"La categoría seleccionada fue {categoria} ")

        pregunta=random.choice(list(preguntas[categoria]))
        print(pregunta.get('pregunta'))
        

        for respuesta in pregunta["respuestas"]:
            print (respuesta)
        
        respuesta_jugador=input(f"ingrese su respuesta (A,B,C,D)\n").upper()
        
        
        return respuesta_jugador, categoria, pregunta

# Funcion principal para realizar la comparacion entre respuesta correcta 
def main():
    
    jugador = input("Ingrese su nombre: \n")
    print(f"Bienvenido {jugador}")
     
    puntos = 0
    
    while True:
        salir = input("Para salir del juego, presione 0. Para continuar pulse cualquier cosa: \n") 
        
        if salir== "0":
            print (f"Gracias por participar {jugador} su puntaje final fue: {puntos} \n")
            break

        respuesta_jugador, categoria, pregunta = Mis_Preguntas(preguntas)

        if respuesta_jugador != pregunta["respuesta correcta"]:
            print (f"La respuesta ingresa es incorrecta :c \n" )

        else :
            print (f"felicidades, su respues es correcta ;)")
        
            puntos +=10
            
        preguntas[categoria].remove(pregunta)
    
    Revision_preguntas(preguntas, categoria)
    
    print(f"¡Su puntuacion fue de {puntos} puntos!") 
    


if __name__ == "__main__":
    main()
