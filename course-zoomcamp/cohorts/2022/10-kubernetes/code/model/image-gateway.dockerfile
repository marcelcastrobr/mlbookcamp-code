#FROM python:3.8.12-slim
FROM suraaga/tensorflow-serving:1.13.0-centos

RUN apt-get update
RUN apt-get upgrade -y
#RUN apt-get install -y python3.8 python3.8-distutils py3-pip
#RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

#RUN pipenv install --system --deploy

COPY ["gateway.py", "proto.py", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "gateway:app"]