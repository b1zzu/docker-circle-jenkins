ARG FROM
FROM ${FROM}

USER root
WORKDIR /

ENV PATH=/opt/node/bin:${PATH}

ARG NODE_VERSION
# 10.16.2 

RUN wget https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.xz \
    && ls -al \
    && tar -vxf  node-v${NODE_VERSION}-linux-x64.tar.xz \
    && rm node-v${NODE_VERSION}-linux-x64.tar.xz \
    && mv node-v${NODE_VERSION}-linux-x64 /opt/node \
    && node --version
