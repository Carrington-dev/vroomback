## Running Celery On Windows With Django

Usually this is harder than described as most information outthere is not relevant to everyone's reasoning.  This provides the simplest way to run celery on windows but running on docker containers

## Items Needed
Inorder to successfully launch a celery email you need to go through these steps

1. __Redis__
There are two ways to run Redis
* Running Redis on docker
```bash
docker run -d -p 6379:6379 --name django-redis -d redis
```
* Using apt-get package on ubuntu/debian
```
sudo apt-get update
sudo apt install redis
sudo systemctl status redis

```
* If you are on windows

```
It's compilcated but very easy
use docker if you have space or this method

Install Redis on Windows
Use Redis on Windows for development

Redis is not officially supported on Windows. However, you can install Redis on Windows for development by following the instructions below.

To install Redis on Windows, you'll first need to enable WSL2 (Windows Subsystem for Linux). WSL2 lets you run Linux binaries natively on Windows. For this method to work, you'll need to be running Windows 10 version 2004 and higher or Windows 11.

Install or enable WSL2
Microsoft provides detailed instructions for installing WSL. Follow these instructions, and take note of the default Linux distribution it installs. This guide assumes Ubuntu.
```

2. __Celery installed__
```
pip install Redis
pip install celery
```
3. __Celery started__
```
celery -A proj worker -l INFO
```
4. __Redis settings__
5. __Celery files settings__
6. __Celery tasks files__
6. __Celery extra notes__
Extra notes on running celery on ubuntu and making sure it runs as a service
```bash
https://www.digitalocean.com/community/questions/how-to-set-up-django-app-redis-celery-a06db780-5335-493e-8158-7128ea7d2cc1
```
Extra notes on celery brokers

```
https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/index.html
```

## Running a web task celery django
```bash
celery -A project_name worker --loglevel=info
# On windows add -P solo 
celery -A project_name worker --loglevel=info -P solo 
```
## Celery Brokers

1. Redis
2. RabbitMQ
```bash
sudo apt-get install rabbitmq-server
```
More notes
```bash
docker run -d -p 5672:5672 rabbitmq
```
3. AmazonSQS etc
```
https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html#choosing-a-broker
```

## Notes links

```bash
https://www.geeksforgeeks.org/celery-integration-with-django/

# more
https://github.com/celery/celery/issues/2832

#
https://circumeo.io/blog/entry/working-with-multiple-celery-queues-in-django/
```