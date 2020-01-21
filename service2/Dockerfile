# Use an official Python runtime as a parent image
FROM python:latest


# Set the working directory to /app
RUN mkdir /service2
#COPY app.py /service2
WORKDIR /service2
# Copy the current directory contents into the container at /app
COPY . /service2

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8081

# Define environment variable
#ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
VOLUME /service2
#ENV FLASK_APP app.py
#ENV FLASK_RUN_HOST 0.0.0.0
#RUN apk add --no-cache gcc musl-dev linux-headers
#COPY requirements.txt requirements.txt
#RUN pip install -r requirements.txt
#COPY . .
#CMD ["flask", "run"]

