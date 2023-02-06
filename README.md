# rest-fastapi

### Start

uvicorn api.main:app --reload

### create & remove container

docker-compose up -d
docker-compose down --volume

### attach container

docker exec -it rest-fastapi-server-1 sh
