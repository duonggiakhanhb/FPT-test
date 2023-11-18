#!/bin/bash

# Build Docker images from Dockerfiles
docker build -t awscli -f Dockerfile.awscli .
docker build -t pyspark -f Dockerfile.pyspark .
docker build -t simple -f Dockerfile.simple .

docker run -it --rm --name awscli awscli