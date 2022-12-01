# Commands

# Conversting h5 model to tflite
```bash 
python convert.py
```
# Generating Docker images

## Creating the docker image for the model
```bash 
docker build -t zoomcamp-10-model:xception-v4-001 -f image-model.dockerfile .
```

## Running the docker image for model
```bash 
docker run --rm -p 8080:8080 clothing-model-v4:v001
```

## Creating the docker image for the gateway
```bash 
docker build -t zoomcamp-10-gateway:002   -f image-gateway.dockerfile .
```
## Running docker image for gateway
```bash 
docker run -it --rm -p 9696:9696 zoomcamp-10-gateway:002
```
## Coping image to kind
```bash 
kind load docker-image zoomcamp-10-gateway:002
```

## Running docker-compose
```bash 
docker-compose up
```
# ECR 
## Authenticate to your default register
```bash 
sudo apt install gnupg2 pass # for ubuntu on ec2
aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin 656001362760.dkr.ecr.eu-west-1.amazonaws.com
```

## Sending my image to ECR
```bash 
aws ecr create-repository --repository-name zoomcamp-10-model-xception-v4-001
docker tag zoomcamp-10-model:xception-v4-001 656001362760.dkr.ecr.eu-west-1.amazonaws.com/zoomcamp-10-model-xception-v4-001
docker push 656001362760.dkr.ecr.eu-west-1.amazonaws.com/zoomcamp-10-model-xception-v4-001


aws ecr create-repository --repository-name zoomcamp-10-gateway-002
docker tag zoomcamp-10-gateway:002 656001362760.dkr.ecr.eu-west-1.amazonaws.com/zoomcamp-10-gateway-002
docker push 656001362760.dkr.ecr.eu-west-1.amazonaws.com/zoomcamp-10-gateway-002
```

# Deploying tf model in local kubernets
```bash 
kubectl apply -f model-deploymemt.yaml 
```
# Check deployment
```bash 
kubectl get pod
```
# Check specific deployment
```bash 
kubectl describe pod tf-serving-clothing-model-86c84f74c5-whwnk
```
# Delete deployment
```bash 
kubectl delete -f model-deploymemt.yaml 
```
# Testing tf-model deployment
```bash 
kubectl port-forward tf-serving-clothing-model-578d7c59dc-66mqm 8500:8500
```
# Testing gateway deployment
```bash 
kubectl port-forward gateway-68f8d4889d-88x8b 9696:9696
```
# Getting inside a pod
```bash 
kubectl exec -it ping-deployment-8685fcdbdb-l5hmm -- bash
```
# Deploying model in EKS

## Create cluster
```bash 
eksctl create cluster -f eks-config.yaml
```
## Delete cluster
```bash 
eksctl delete cluster --name mlzoomcamp-eks
```