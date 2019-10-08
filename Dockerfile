FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

EXPOSE 80
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "Fase3/flask/__init__.py" ]