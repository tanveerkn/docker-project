# Use an official Python runtime as a parent image
FROM python:latest


# Set the working directory to /app
WORKDIR /service1/
#ADD service1.py /service1/
#ADD index.html /server/

# Copy the current directory contents into the container at /app
COPY . /service1

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8080

# Define environment variable
#ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]

#ENV FLASK_APP app.py
#ENV FLASK_RUN_HOST 0.0.0.0
#RUN apk add --no-cache gcc musl-dev linux-headers
#COPY requirements.txt requirements.txt
#RUN pip install -r requirements.txt
#COPY . .
#CMD ["flask", "run"]
