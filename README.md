# Ca dealer Exchange API

This includes authentication with the following endpoints

## Auth Endpoints </>
```bash
#  Under nginx docker-compose
/api/v1/auth/users/ # all users
/api/v1/auth/users/me/ # all users
/api/v1/auth/users/me/ # all users
/api/v1/auth/jwt/create/
/api/v1/auth/jwt/refresh/
```

## Forex API 

```bash
#  Under nginx docker-compose
/forex/
/forex/api/v1/forex/
/forex/api/v1/forex/currencies/
/forex/api/v1/forex/currencies/<currency-name>
/forex/api/v1/forex/currencies/ZAR/

```

## Vroomhive API 

```bash
#  Under nginx docker-compose

{
    "countries": "http://api.vroomhive.co.za/api/v1/countries/",
    "cities": "http://api.vroomhive.co.za/api/v1/cities/",
    "states": "http://api.vroomhive.co.za/api/v1/states/",
    "makes": "http://api.vroomhive.co.za/api/v1/makes/",
    "brands": "http://api.vroomhive.co.za/api/v1/brands/",
    "vehicles": "http://api.vroomhive.co.za/api/v1/vehicles/",
    "models": "http://api.vroomhive.co.za/api/v1/models/",
    "user_vehicles": "http://api.vroomhive.co.za/api/v1/user_vehicles/",
    "enquiries": "http://api.vroomhive.co.za/api/v1/enquiries/",
    "variants": "http://api.vroomhive.co.za/api/v1/variants/"
}

```
## API-KEY Authentication

Managed to add API-KEY authentication via X-Api-Key on headers. Also managed to add user authentication with token based authentication with djoser and simple-jwt on one simple container

```bash
# 
# Example of API-KEYs <FIXs0Rft.UwfTi7EMNy0tA3caoIq9jh1a6JIuwbut>
# Once created it should be stored otherwise you won't be able to see it again
```


## Project Structure

```python
/cardealer # forex APIs
/authenticate # authentication APIs
/nginx # merges two api into one domain
docker-compose.yaml
```

## Project Exploration

To explore using different domains/sub-domains for each service
```bash
api.vroomhive.co.za
auth.vroomhive.co.za
# Just an idea
```

## Car=Dealership

__Endpoints__
```bash
# admin
/clients

to allow user to access /clients change is_staff to true
```

## Initial Commands

```bash
python manage.py create_countries 
python manage.py create_makes 
```

```bash
authgunicorn -> auth.vroomhive.co.za
newsgunicorn -> news.vroomhive.co.za
gunicorn -> api.vroomhive.co.za
```

## Tokens

```bash
curl -X GET http://127.0.0.1:8001/api/v1/auth/users/me/ -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzODA2MDExLCJpYXQiOjE3MjM2MzMyMTEsImp0aSI6IjNkODBlNDg0ZjY2YzQ3YzNiODgyZTIzODI0NDhhYzJkIiwidXNlcl9pZCI6ImI3MTlhNzMzLTNhOWYtNGQxMS05OWRiLWU2MGFiMDVhNGZjYiJ9.FkacsGZNsCAo0gh7HSYxcmb6ywvoTaCIVvCx3AE981c'


curl -X GET -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzNjMyNzE5LCJpYXQiOjE3MjM2MzI0MTksImp0aSI6IjRmYmFkYjRiOTFlNjQ3OWI5MzQ1MTVlNTI1NzcxNTRmIiwidXNlcl9pZCI6ImI3MTlhNzMzLTNhOWYtNGQxMS05OWRiLWU2MGFiMDVhNGZjYiJ9.21h3I0nzfptJQG5IwjQdz7bYa6lEw_--KzB7pWOmrto" "http://localhost:8001/api/v1/users/me"
```

## Understand DBshell
```bash
python manage.py dbshell
https://fig.io/manual/django-admin/dbshell


docker run --hostname=0bf79f2334c7 --mac-address=02:42:ac:11:00:03 --env=POSTGRES_PASSWORD=#Mulalo96 --env=POSTGRES_DB=vroomhive_cardealer --env=POSTGRES_USER=root --env=PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/postgresql/16/bin --env=GOSU_VERSION=1.17 --env=LANG=en_US.utf8 --env=PG_MAJOR=16 --env=PG_VERSION=16.3-1.pgdg120+1 --env=PGDATA=/var/lib/postgresql/data --volume=/var/lib/postgresql/data -p 5432:5432 --restart=no --runtime=runc -d postgres

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE news_contact (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(), -- Requires the `uuid-ossp` extension
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    subject VARCHAR(300) NOT NULL,
    phone VARCHAR(30) NOT NULL,
    notes TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

```