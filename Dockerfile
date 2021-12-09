# Imagen base
FROM ubuntu
# Descargar e instalar dependencias
RUN mkdir /arangodb1
WORKDIR /arangodb1
RUN apt-get -qq update
RUN apt install -qq -y python3
RUN apt install -qq -y python3-pip
RUN pip install -qq python-arango
ADD main.py /arangodb1

# Comando de arranque
CMD ["python3","main.py"]
