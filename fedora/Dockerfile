ARG FEDORA_VERSION
FROM fedora:${FEDORA_VERSION}

RUN dnf -y install \
        wget \
        unzip \
        xz \
    && dnf clean all
