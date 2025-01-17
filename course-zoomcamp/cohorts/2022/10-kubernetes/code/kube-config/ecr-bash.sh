ACCOUNT_ID=656001362760
REGION=eu-west-1
REGISTRY_NAME=mlzoomcamp-images
PREFIX=${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${REGISTRY_NAME}

GATEWAY_LOCAL=zoomcamp-10-gateway:002
GATEWAY_REMOTE=${PREFIX}:zoomcamp-10-gateway-002
docker tag ${GATEWAY_LOCAL} ${GATEWAY_REMOTE}

MODEL_LOCAL=zoomcamp-10-model:xception-v4-001
MODEL_REMOTE=${PREFIX}:zoomcamp-10-model-xception-v4-001
docker tag ${MODEL_LOCAL} ${MODEL_REMOTE}

docker push ${MODEL_REMOTE}
docker push ${GATEWAY_REMOTE}