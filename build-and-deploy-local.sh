#!/usr/bin/env bash

# set the environment of the minikube docker
eval $(minikube docker-env)

# build the docker image
docker build --tag ultimaker/mongo-operator:local .

# print out the Kubernetes client and server versions
kubectl version

# remove the deployment, if needed, and apply the new one
kubectl delete deployment mongo-operator 2>/dev/null
kubectl apply --filename=kubernetes/operators/mongo-operator/service-account.yaml
kubectl apply --filename=kubernetes/operators/mongo-operator/cluster-role.yaml
kubectl apply --filename=kubernetes/operators/mongo-operator/cluster-role-binding.yaml
kubectl apply --filename=kubernetes/operators/mongo-operator/deployment.yaml

# show some details about the deployment
kubectl describe deploy mongo-operator

# wait for the pod to startup to retrieve its name
sleep 10
POD_NAME=$(kubectl get pods | grep -e "mongo-operator.*Running" | cut --fields=1 --delimiter=" ")

# apply the example file, scale it up in 30 seconds and scale down in 60
kubectl apply --filename=examples/mongo-3-replicas.yaml
(sleep 30; kubectl apply --filename=examples/mongo-5-replicas.yaml)&
(sleep 60; kubectl apply --filename=examples/mongo-3-replicas.yaml)&

# show the pod logs
kubectl logs ${POD_NAME} --follow
