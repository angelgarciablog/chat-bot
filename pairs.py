import re

basicos = [
    [r'^(Hola|Hola|Buenos días|Buenas tardes|Buenas noches)$', ['Hola, ¿cómo estás?', 'Hola, ¿qué tal estás?', 'Buenos días, ¿cómo estás?']],
    [r'^soy (.*)$', ['Hola, mucho gusto ', 'Hola ', 'Buenos días, ¿cómo estás %1 ?']],
    [r'(bien|muy bien|super)$',['me alegra, en que te puedo ayudar','me alegra']],
    [r'^(¿Cómo estás\?|¿Qué tal estás\?)$', ['Estoy bien, ¿y tú?', 'Estoy bien, gracias por preguntar.']],
    [r'^(¿De dónde eres\?|¿De dónde eres\?|¿De dónde eres originario\?)$', ['Soy de Nicaragua.', 'Soy originario de Nicaragua.']],
    [r'^(¿Cuántos años tienes\?|¿Cuántos años tienes\?|¿Cuál es tu edad\?)$', ['Tengo 22 años.', 'Tengo 22 años de edad.']],
    [r'^(¿Qué tal tu día\?|¿Cómo estuvo tu día\?)$', ['Mi día estuvo bien, ¿y el tuyo?']],
    [r'^(¿Qué te gusta hacer\?|¿Cuáles son tus pasatiempos\?)$', ['Me gusta leer, escribir, hacer deporte y viajar.', 'Mis pasatiempos incluyen leer, escribir, hacer deporte y viajar.']],
    [r'^(¿A qué te dedicas\?|¿Cuál es tu trabajo\?)$', ['Soy estudiante.', 'Trabajo como programador.']],
    [r'^(¿Qué te gusta de tu trabajo\?|¿Qué te gusta de tu trabajo\?)$', ['Me gusta la creatividad y la variedad que me ofrece mi trabajo.', 'Lo que más me gusta de mi trabajo es la creatividad y la variedad que me ofrece.']]
]



pairs = [
    ['¿Qué es WhatsApp?', ['WhatsApp es una aplicación de mensajería instantánea para teléfonos inteligentes que permite enviar y recibir mensajes, imágenes, videos, audios, grabaciones de audio, documentos, ubicaciones, contactos, gifs, stickers, así como realizar llamadas y videollamadas con varios participantes a la vez.']],
    ['¿Cuándo se lanzó WhatsApp?', ['WhatsApp se lanzó en 2009 principalmente para iOS y en 2010 para Android. Se popularizó masivamente a partir de 2012.']],
    ['¿Cuántos usuarios tiene WhatsApp?', ['A principios de 2020, WhatsApp tenía más de 2 mil millones de usuarios en todo el mundo, superando a otras aplicaciones como Facebook Messenger o Telegram.']],
    ['¿Quién es dueño de WhatsApp?', ['WhatsApp fue adquirida por la empresa Meta (ahora conocida como Facebook) en 2014 por un valor de 19.000 millones de dólares.']]
]

#abreviaturas usadas por usuarios
"""
abreviaturas = {
    "cm": "como",
    "x": "por",
    "xq": "por que",
    "dond": "donde",
    "etc": "exetera",
    "q": "qué",
    "Q": "Qué",
    "k": "que"
    
}
"""

# Agregar reflexiones en español
reflections_es = {
  'Soy': 'Eres',
  'soy': 'eres',
  'estoy': 'estás',
  'fui': 'fuiste',
  'era': 'eras',
  'Yo': 'Tú',
  'yo': 'tú'
}
reflections_es