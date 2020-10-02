# OpenPose API
Simple containerized REST API extracting (and draw) [CMU OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose/) (human pose) key-points from images (provided as file or url). 
This version is GPU accelerated, using CUDA (10.0) and CuDNN (7.5) compatible hardware, allowing to e

## DocaPrerequisites
Other container orchestration software, like Kubernetes may also be used, but Docker is the easiest. 
- Nvidia GPU and drivers on the Host. 
- [Docker](https://docs.docker.com/get-docker/)
- [Nvidia Docker Runtime](https://github.com/NVIDIA/nvidia-docker)
- [docker-compose](https://docs.docker.com/compose/install/)
 
## Getting Started
```
git clone https://github.com/lyngon/openpose-api.git
cd openpose-api
docker-compose up -d
```

In a browser visit `http://localhost:8080/docs`. Assuming the browser is running on the same machine.
If everything worked, you should see an interactive Swagger documentation wehere you can try out the API.  

## To Do
- Generalize to also run on CPU 
- Kubernetes example


