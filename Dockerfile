FROM python:3.11.2

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory in the container
WORKDIR /code

# Copy requirements.txt
COPY ./requirements.txt /code/requirements.txt

# Install python dependencies
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt

# Copy the current directory contents into the container at /code
COPY . /code/

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

