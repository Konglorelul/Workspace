If you are running minikube on docker, make sure to enable the ports when starting.

```sh
minikube start --driver=docker --ports=30487:30487
kubectl proxy --address=0.0.0.0 --accept-hosts='.*' &
redis-cli -h $(minikube ip) -p 30487 PING
```