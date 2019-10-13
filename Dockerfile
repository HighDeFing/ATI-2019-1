FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

#EXPOSE 80
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
COPY ./fase4-jugar/imple/import.sh /docker-entrypoint-initdb.d/
CMD mongoimport --db Trivias --collection Trivia11 --drop --file ./fase4-jugar/imple/trivias11.json --jsonArray
CMD mongoimport --db Trivias --collection Categorias --drop --file ./fase4-jugar/imple/categoria.json --jsonArray
#EXPOSE 27017

#CMD ["mongod", "--smallfiles"]
#CMD ["python", "Fase3/flask/__init__.py" ]