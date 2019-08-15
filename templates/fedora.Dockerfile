ARG VERSION
FROM fedora:${VERSION}

RUN dnf -y install \
        wget \
        unzip \
    && dnf clean all
