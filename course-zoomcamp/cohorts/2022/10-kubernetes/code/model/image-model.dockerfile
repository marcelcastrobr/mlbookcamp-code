FROM tensorflow/serving:latest

COPY clothing-model /models/clothing-model/1
ENV MODEL_NAME="clothing-model"