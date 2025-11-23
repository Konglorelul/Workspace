# Workspace

Repository purposed for ongoing and finished personal projects.

## Description

The repository is meant to be the workspace for my personal projects. Here you will find everything from small scripts to python packages and testing of everything i do. Documentation directory contains certain details about each finalized project.

## Reminder change kubeconfig
```sh
cat > ./minikube-lens.yaml <<EOF
apiVersion: v1
kind: Config
clusters:
- cluster:
    server: http://$(hostname -I | awk '{print $1}'):8001
  name: minikube
contexts:
- context:
    cluster: minikube
    user: default
  name: minikube
current-context: minikube
users:
- name: default
  user: {}
EOF
```
