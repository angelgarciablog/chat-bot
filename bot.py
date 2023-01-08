import nltk
from nltk.chat.util import Chat, reflections
import random

from difflib import SequenceMatcher, get_close_matches
import re
from pairs import basicos, pairs, reflections_es


#pares por defecto
default_pairs = [
    ["Hola, ¿cómo estás?", ["Hola, estoy bien. ¿Y tú?", "Hola, estoy genial gracias por preguntar."]],
    ["¿De qué te gusta hablar?", ["Me gusta hablar de muchos temas, como tecnología, ciencia, libros, películas, etc."]],
    ["Hola", ["Hola. bienvenido,¿como puedo ayudarte?","Hola bienvenido"]],
]

pairs = pairs + basicos #agrega aqui tus pairs sobre el tema especifico para el que se usara el bot:


def preguntas(pairs):
    preguntas=[]
    for a, b in enumerate(pairs):
        preguntas.append(b[0])
    return preguntas

def Similitud(mensaje, pairs):
    lista_key = preguntas(pairs)
    
    considencias = get_close_matches(mensaje, lista_key, n=1, cutoff=0.5)
    if len(considencias) > 0:
        
        puntuacion = SequenceMatcher(None,mensaje ,considencias[0])
        porsentaje = '{:.2f}'.format(0.8542*100)

        return considencias[0] ,porsentaje
    else:
        return None
    

def default_response():
    return "Lo siento, no entiendo lo que quieres decir."
def chatiar(mensaje,chat,pairs):
    consulta = chat.respond(mensaje)
    if consulta:
        return consulta
    else:
        similitud = Similitud(mensaje,pairs)
        if similitud:
            #para optener el porsentaje de similitud usa 'similitud[2]'
            pregunta = similitud[0]
            resp = chat.respond(pregunta)
            respuesta =r"Respondiendo a : %s /t %s " %(pregunta,resp)
            return respuesta
        
    

chatbot = Chat(pairs, reflections_es)

while True:
    msj = str(input(">> " ))
    print(chatiar(mensaje=msj,chat=chatbot,pairs=pairs))
