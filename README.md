# Microservices using Kubernetes and Python

Microservice architecture to convert video to audio using Kubernetes and Python




## Tech Stack

**Language:** Python

**Tools:** Kubernetes, Docker, RabbitMQ

**DB:** MySQL, MongoDB



## Architecture

![system design](https://github.com/AshiishKarhade/Microservice-video-to-audio-using-Kubernetes-and-Python/blob/main/architecture.svg)



## Run Locally

Install Tools

- Docker
- Kubernetes
- MySQL
- MongoDB


Clone the project

```bash
  git clone https://github.com/AshiishKarhade/Microservices-with-Kubernetes-and-Python.git
```

Go to the project directory

```bash
  cd Microservices-with-Kubernetes-and-Python
```

Start minikube tunnel

```bash
  minikube tunnel
```

Start K8S services

```bash
  kubectl apply -f /auth/manifests/
  kubectl apply -f /gateway/manifests/
  kubectl apply -f /converter/manifests/
  kubectl apply -f /rabbit/manifests/
  kubectl apply -f /notification/manifests/
```

## Authors

- [@ashiishkarhade](https://www.github.com/ashiishkarhade)



