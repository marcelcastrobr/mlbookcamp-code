#FROM tensorflow/serving:latest
FROM suraaga/tensorflow-serving:1.13.0-centos

COPY clothing-model /models/clothing-model/1
ENV MODEL_NAME="clothing-model"