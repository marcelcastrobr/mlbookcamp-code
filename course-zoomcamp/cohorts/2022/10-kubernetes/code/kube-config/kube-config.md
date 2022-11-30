# Commands

# Conversting h5 model to tflite
python convert.py

# Generating Docker images

## Creating the docker image for the model
sudo docker build -t clothing-model-v4:v001 .

## Running the docker image for model
sudo docker run --rm -p 8082:8080 clothing-model-v4:v001


## Creating the docker image for the gateway
sudo docker build -t zoomcamp-10-gateway:002   -f image-gateway.dockerfile .

## Running docker image for gateway
docker run -it --rm -p 9696:9696 zoomcamp-10-gateway:002

## Coping image to kind
sudo kind load docker-image zoomcamp-10-gateway:002

# Sending my image to ECR
aws ecr create-repository --repository-name tf-clothing-model-v4-v001

sudo docker tag clothing-model-v4:v001 656001362760.dkr.ecr.eu-west-1.amazonaws.com/tf-clothing-model-v4-v001

sudo docker push 656001362760.dkr.ecr.eu-west-1.amazonaws.com/tf-clothing-model-v4-v001


# Deploying tf model in local kubernets
sudo kubectl apply -f model-deploymemt.yaml 

# Check deployment
sudo kubectl get pod

# Check specific deployment
sudo kubectl describe pod tf-serving-clothing-model-86c84f74c5-whwnk

# Delete deployment
sudo kubectl delete -f model-deploymemt.yaml 

# Testing tf-model deployment
sudo kubectl port-forward tf-serving-clothing-model-578d7c59dc-66mqm 8500:8500

# Getting inside a pod
sudo kubectl exec -it ping-deployment-8685fcdbdb-l5hmm -- bash