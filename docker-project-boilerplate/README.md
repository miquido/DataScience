# Boilerplate for datascience projects using docker.

This project basic setup is based on:
 - [All-in-one Docker image for Deep Learning](https://github.com/floydhub/dl-docker)
 - [Tensorflow docker files](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/tools/dockerfiles/dockerfiles)

----
#### Building image: 
0. Install Docker & start docker daemon
1. Build image: ```docker build -f Dockerfile ./ -t 'ds-default:cpu' ```


#### Run container from build image
```docker run -it -p 8888:8888 -v $(pwd):/root/ ds-default:cpu ```

| Parameter      | Explanation |
|----------------|-------------|
|`-it`             | This creates an interactive terminal you can use to iteract with your container |
|`-p 8888:8888 `    | This exposes the ports inside the container so they can be accessed from the host. The default iPython Notebook runs on port 8888 and Tensorboard on 6006 |
|`-v $(pwd):/root/` | This shares the whole project root folder `$(pwd)` on your host machine to `/root` inside your container. Any data written to this folder by the container will be persistent. 
|`ds-default:cpu`   | This the image that you want to run. The format is `image:tag`. In our case, we use the image `dl-docker` and tag `gpu` or `cpu` to spin up the appropriate image |



---


#### Running jupyter notebook backend inside container - develop locally in browser:
 1. inside container ```jupyter notebook --notebook-dir=/notebooks --ip 0.0.0.0 --no-browser --allow-root"```
 2. enter [http://localhost:8888/](http://localhost:8888/) or logged in console link with token
 
 
---- 
 
 #### Usefull commands:
 
 | command     | effect |
 |-------------|--------|
 |```docker ps``` | list all running containers, add flag ```-a``` to list all containers|
 |```docker rm $(docker ps -a -q)``` | remove all containers|
 | ```docker rmi $(docker images -q)```| remove all images|
 |``` docker exec -it <container-id>```| enter running container|
 
 
 