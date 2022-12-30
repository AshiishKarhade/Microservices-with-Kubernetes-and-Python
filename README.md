# Microservices using Kubernetes and Python

Microservice architecture to convert video to audio using Kubernetes and Python

This video to audio converter service is a powerful and reliable platform for converting video files into audio format. Built with Python and designed to be highly scalable and reliable, our service is an essential tool for anyone looking to convert their video files into audio format quickly and easily.

To use our service, clients simply need to interact with our API gateway. The gateway will authenticate and authorize the user, ensuring that only authorized users have access to the service. Once the user is authenticated, they can upload a video file to the service, which will be stored in our MongoDB database.

The video to audio service will then pull the video from the database, and using our video-to-audio conversion service, will convert the video into audio format. Once the conversion is complete, the service will send a message to RabbitMQ, notifying the user that the video has been converted and is ready for download.

The entire architecture of our service is containerized using Docker and deployed using Kubernetes, which makes it highly scalable and reliable. Whether you're a business, a content creator, or an individual, our video to audio converter service has you covered



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



