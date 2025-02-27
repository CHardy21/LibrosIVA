# Un archivo docker (dockerfile) comienza siempre importanto la imagen base. 
# Utilizamos la palabra clave 'FROM' para hacerlo.
# En nuestro ejemplo, queremos importar la imagen de python.
# Así que escribimos 'python' para el nombre de la imagen y ':x.x-...' para la versión.

FROM python:3.12

# Instalar dependencias necesarias 
RUN apt-get update && apt-get install -y \ xvfb \ x11-utils

# Establecemos el path de  nuestro proyecto dentro del contenedor.

WORKDIR /code

# Para lanzar nuestro código python, debemos importarlo a nuestra imagen.
# Utilizamos la palabra clave 'COPY' para hacerlo.
# El primer parámetro 'main.py' es el nombre del archivo en el host.
# El segundo parámetro '/' es la ruta donde poner el archivo en la imagen.
# Aquí ponemos el archivo en la carpeta raíz de la imagen. 
COPY . /code

RUN pip install --no-cache-dir -r requirements.txt

# Necesitamos definir el comando a lanzar cuando vayamos a ejecutar la imagen.
# Utilizamos la palabra clave 'CMD' para hacerlo.
# El siguiente comando ejecutará "python ./main.py".

#CMD [ "python", "app.py" ]

# Iniciar Xvfb y luego ejecutar tu aplicación
CMD ["sh", "-c", "Xvfb :99 -screen 0 1024x768x16 & python app.py"]