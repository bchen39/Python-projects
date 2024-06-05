# Tor Exit Node Management

A simple Flask web app that utilizes RESTful API to support search, delete, and retrieve tor exit nodes from a list. Also includes background refresh functionality.

# Building Docker Image

```bash
docker build -t tor-checker .
docker run -dp 127.0.0.1:5000:5000 tor-checker
```

# Usage:

## Retrieve tor exit node list: 

`127.0.0.1:5000/list`

## Search for ip in list: 

`127.0.0.1:5000/search?ip=ip_address`

e.g. `127.0.0.1:5000/search?ip=0.0.0.0` if address is IPv4 or `127.0.0.1:5000/search?ip=2a0b:f4c2:0000:0000:0000:0000:0000:0028` if address is IPv6

## Delete ip from list: 

`127.0.0.1:5000/delete?ip=ip_address`

e.g. `127.0.0.1:5000/delete?ip=0.0.0.0` if address is IPv4 or `127.0.0.1:5000/delete?ip=2a0b:f4c2:0000:0000:0000:0000:0000:0028` if address is IPv6

The list automatically refreshes every 5 minutes, after which the previously deleted values will still remain deleted.

# Stopping container

```bash
docker ps 
# copy the container id shown in ps
docker stop container_id
docker rm container_id
```