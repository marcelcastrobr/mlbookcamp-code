# Simple PING Deployment using Kubernets

## Starting the deployment
sudo kubectl -f deployment.yaml

## Cheking your deployment
sudo kubectl get pod 

or

sudo kubectl describe <deployment-name>

### Test PING using port-forwarding
sudo kubectl <deployment-name> 9696:9696

## Starting the service
sudo kubectl apply -f service.yaml

## Checking service
sudo kubectl get svc
or 
sudo kubectl get service

### Test PING using port-forwarding for service
sudo kubectl port-forward service/ping 8081:80

