## FastAPI + PostgreSQL + Docker template

### Install

```
touch .env
```

modify `.env` file

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=rest-fastapi
HOST=postgres
PORT=5432
PYTHONPATH=/app
```

### Start

```
docker-compose up -d --build
```

### Down container with volume

```
docker-compose down --volume
```

### Create migration file

```
docker-compose exec server alembic revision --autogenerate -m 'create profile'
```

### Test

```
docker-compose exec server pytest .
```
