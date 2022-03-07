# pull official base image

FROM cwaffles/openpose

ARG app_name=api

# set working directory
RUN mkdir -p /usr/src
WORKDIR /usr/src

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# install python dependencies
RUN pip3 install --upgrade pip
COPY ./requirements.txt .
COPY ./requirements-test.txt .
COPY ./requirements-dev.txt .
RUN pip3 install -r requirements-dev.txt
# RUN pip3 install python-multipart

# add app
COPY . .

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN ln -s /openpose/build/python/openpose/pyopenpose.cpython-36m-x86_64-linux-gnu.so /usr/local/lib/python3.6/dist-packages/


# run entrypoint.sh
ENTRYPOINT ["/usr/src/entrypoint.sh"]
