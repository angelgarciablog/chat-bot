# Chat bot con nltk 

version 0.1.1

Este es un ejemplo de chat bot usando nltk y Python, los usos que le podemos dar son muy variados

## Requisitos

Para utilizar este proyecto, necesitará tener lo siguiente instalado en su sistema:

- Python 3.11 (probablemente funcione con cualquier version superior a Python 3.8)
- Virtualenv (para crear entornos virtuales)

## Creación de un entorno virtual

Es recomendable crear un entorno virtual para este proyecto, ya que esto aislará las dependencias del proyecto de las demás dependencias en su sistema.

### Windows

1. Abra una consola y navegue hasta la carpeta del proyecto.
2. Ejecute el comando `python -m venv nombre_del_entorno`. Esto creará un entorno virtual con el nombre especificado en la carpeta del proyecto.
3. Active el entorno virtual ejecutando el comando `nombre_del_entorno\Scripts\activate.bat`.

### MacOS y Linux

1. Abra una terminal y navegue hasta la carpeta del proyecto.
2. Ejecute el comando `python3 -m venv nombre_del_entorno`. Esto creará un entorno virtual con el nombre especificado en la carpeta del proyecto.
3. Active el entorno virtual ejecutando el comando `source nombre_del_entorno/bin/activate`.

## Instalación de dependencias

Una vez que se ha creado y activado el entorno virtual, instale las dependencias del proyecto ejecutando el siguiente comando:

```pip install -r requirements.txt```


Este comando instalará todas las dependencias especificadas en el archivo `requirements.txt` en el entorno virtual.

## Inicio del proyecto

Para iniciar el proyecto, ejecute el siguiente comando en la consola:

```python bot.py```

Este comando ejecutará el archivo `bot.py` y iniciará el chat en consola.

# reentrenar el bot con otro contenido: 
actualmente no se a implementado un mecanismo de entrenamiento en este bot .
-puedes tokenizar un texto con chat-gpt3 usando el siguiente mensaje.

`Crea una lista de pares para nltk usando la siguiente información: ........`
es importante revisar que los token generados por chat-gpt3. en algunas ocasiones hace falta algunos caracteres como llaves o comas.

-agrega tus pairs generados por chat-gpt3 en el archivo `pairs.py`
los token de ejemplo usados en este bot fueren generados con el texto que esta en el activado `text_de_entrenamiento.txt`


