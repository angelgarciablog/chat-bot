import re
import nltk
from nltk.chat.util import Chat, reflections

# Crear una lista de pares de diálogo utilizando expresiones regulares
pairs = [
    [r'(Hola|Buenos días|Buenas tardes|Buenas noches)', ['Hola, ¿cómo estás?', 'Hola, ¿qué tal?']],
    [r'(¿Cómo estás\?|¿Qué tal\?)', ['Estoy bien, gracias. ¿Y tú?', 'Estoy bien, gracias. ¿Qué hay de nuevo?']],
    [r'(Sí|No)', ['¿Por qué sí?', '¿Por qué no?']],
]

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

# Crear el bot
bot = Chat(pairs, reflections_es)

# Iniciar el bot
bot.converse()
