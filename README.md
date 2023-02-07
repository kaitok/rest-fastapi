# rest-fastapi

### Start

`uvicorn api.main:app --reload`

### create & build container

docker-compose up -d --build

### down container with volume

docker-compose down --volume

### attach container

docker-compose exec -it server sh

### create migration file

docker-compose exec server alembic revision --autogenerate -m 'create profile'
