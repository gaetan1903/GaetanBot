#Grab the latest ubuntu image
FROM ubuntu:latest

# Install python and pip
RUN apt update && apt install -y python3 python3-pip git
ADD ./requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

# Expose the port that you need
EXPOSE 80

# Add our code
WORKDIR /opt/
git clone https://github.com/gaetan1903/GaetanBot.git

		
CMD gunicorn --bind 0.0.0.0:80 wsgi 
