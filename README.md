# django-scenes
Create the map for my text adventure and expose it as thrift service

## Requirements
to run this quick you will need
- docker
- docker-compose

## starting this using docker
### get the docker image running
```
docker-compose up
```
### find the docker image id to get in there (usually the first)
```
docker ps
```

### get in that container
```
# example <ID> djangoscenes_web_1 ususally under the NAMES column as previous output
docker exec -it <ID> bash
```

### create super user
```
python manage.py createsuperuser
```
