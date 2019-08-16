ARG FROM_IMAGE
FROM ${FROM_IMAGE}

ENV PATH=/opt/docker:${PATH}

ARG DOCKER_VERSION

RUN wget https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz \
    && tar -xvf docker-${DOCKER_VERSION}.tgz \
    && rm docker-${DOCKER_VERSION}.tgz \
    && mv docker /opt/docker \
    && docker --version
