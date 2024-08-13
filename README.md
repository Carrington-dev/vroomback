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
forex.vroomhive.co.za
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