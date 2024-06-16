# # Use an official Python runtime as a parent image
# FROM python:3.12.1

# # Set the working directory in the container
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . .

# # Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt

# # Make port 8000 available to the world outside this container
# EXPOSE 8000

# # Run manage.py to start the server
# # CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# # Collect static files
# RUN python manage.py collectstatic --noinput

# # Run Django application
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "foreweb.wsgi:application"]