FROM python:2.7

#RUN apt-get update -y && \
#    apt-get install -y python-pip python-dev

# EXPOSE 5000
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
#EXPOSE 27017

#CMD ["mongod", "--smallfiles"]

#CMD ["python", "Fase3/flask/__init__.py" ]