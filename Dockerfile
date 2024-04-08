FROM python:3.11.4-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY . /app/

RUN apt-get update \
    && apt-get install -y libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .
RUN pip install -r requirements.txt






# # Use a lightweight Python base image
# FROM python:3.9

# # Create a working directory within the container
# WORKDIR /app

# # Copy the project code
# COPY . .

# # Install dependencies from requirements.txt
# RUN pip install -r requirements.txt

# # Expose the Django development port (default: 8000)
# EXPOSE 8000

# # Start the Django development server (assuming manage.py)
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]









# # Use the official Python image as the base image
# FROM python:3.9

# # Set working directory in the container
# WORKDIR /code

# # Copy requirements.txt file to the container
# COPY requirements.txt .

# # Install dependencies from requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the Django project code to the container
# COPY . .

# # Expose port 8000 to the outside world (optional, adjust if using a different port)
# EXPOSE 8000

# # Command to run your Django application (modify as needed)
# CMD ["python", "manage.py", "runserver"]


