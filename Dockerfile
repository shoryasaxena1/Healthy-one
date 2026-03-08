# Use an official Python image
FROM python:3.10-slim

# Set the folder where our code will live on the server
WORKDIR /app

# Copy our files from the phone to the server
COPY . /app

# Install the tools listed in our requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Tell the server to run our website
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]

