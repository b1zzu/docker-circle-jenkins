ARG FROM_IMAGE

FROM buildpack-deps:18.10 AS make

ARG PYTHON_VERSION

RUN wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tar.xz \
    && tar -vxf Python-${PYTHON_VERSION}.tar.xz \
    && cd Python-${PYTHON_VERSION} \
    && ./configure --prefix /opt/python \
    && make \
    && make install

FROM ${FROM_IMAGE}

USER root
WORKDIR /

ENV PATH=/opt/python/bin:${PATH}

COPY --from=make /opt/python /opt/python

RUN python3 --version
