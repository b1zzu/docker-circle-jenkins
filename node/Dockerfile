ARG FROM_IMAGE
FROM ${FROM_IMAGE}

USER root
WORKDIR /

ENV PATH=/opt/node/bin:${PATH}

ARG NODE_VERSION

RUN wget https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.xz \
    && tar -vxf node-v${NODE_VERSION}-linux-x64.tar.xz \
    && rm node-v${NODE_VERSION}-linux-x64.tar.xz \
    && mv node-v${NODE_VERSION}-linux-x64 /opt/node \
    && node --version
