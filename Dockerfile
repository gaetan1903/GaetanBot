#Grab the latest ubuntu image
FROM ubuntu:latest

# Install python and pip
RUN apt update && apt install -y python3 python3-pip 
ADD ./requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

# Add our code
ADD * /opt/
WORKDIR /opt/

		
CMD gunicorn --bind 0.0.0.0:80 wsgi 
