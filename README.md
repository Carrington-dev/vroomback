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

## Tokens

```bash
curl -X GET http://127.0.0.1:8001/api/v1/auth/users/me/ -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzODA2MDExLCJpYXQiOjE3MjM2MzMyMTEsImp0aSI6IjNkODBlNDg0ZjY2YzQ3YzNiODgyZTIzODI0NDhhYzJkIiwidXNlcl9pZCI6ImI3MTlhNzMzLTNhOWYtNGQxMS05OWRiLWU2MGFiMDVhNGZjYiJ9.FkacsGZNsCAo0gh7HSYxcmb6ywvoTaCIVvCx3AE981c'


curl -X GET -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzNjMyNzE5LCJpYXQiOjE3MjM2MzI0MTksImp0aSI6IjRmYmFkYjRiOTFlNjQ3OWI5MzQ1MTVlNTI1NzcxNTRmIiwidXNlcl9pZCI6ImI3MTlhNzMzLTNhOWYtNGQxMS05OWRiLWU2MGFiMDVhNGZjYiJ9.21h3I0nzfptJQG5IwjQdz7bYa6lEw_--KzB7pWOmrto" "http://localhost:8001/api/v1/users/me"
```