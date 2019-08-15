ARG VERSION
FROM fedora:${VERSION}

RUN dnf -y install \
        wget \
        unzip \
        xz \
    && dnf clean all
