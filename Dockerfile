ARG IMAGE_REPOSITORY=python
ARG IMAGE_TAG=3.7-alpine3.9

FROM ${IMAGE_REPOSITORY}:${IMAGE_TAG}
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apk update && apk add postgresql-dev python3-dev
RUN mkdir /code
ADD requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt
ADD . /code/
