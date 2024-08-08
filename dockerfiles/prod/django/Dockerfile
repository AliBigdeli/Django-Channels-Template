FROM python:3.10-slim-buster

LABEL maintainer="bigdeli.ali3@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app


COPY ./requirements.txt .
RUN pip3 install   --upgrade pip && \
    pip3 install   -r requirements.txt 

COPY ./core/ .

# Copy entrypoint script
COPY ./dockerfiles/prod/django/entrypoint.sh .

# Give execute permission to the entrypoint script
RUN chmod +x ./entrypoint.sh

# Set entrypoint to the script
ENTRYPOINT ["./entrypoint.sh"]
