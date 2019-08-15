#!/usr/bin/env bash

set -e
set -x

VERSION=${VERSION:-alpha}
NAMESPACE=${NAMESPACE:-}

OPENJDK_VERSION=${1:-8}
FEDORA_VERSION=${2:-31}

if [ ${OPENJDK_VERSION} == 8 ]; then
    OPENJDK_TEMPLATE=openjdk8
else
    echo "error: only 8 is supported"
    exit 1
fi

FEDORA_IMAGE=$(./images/fedora.sh ${FEDORA_VERSION})

OPENJDK_IMAGE=${NAMESPACE}openjdk:${VERSION}-fedora${FEDORA_VERSION}-openjdk${OPENJDK_VERSION}

docker build \
    --build-arg FROM=${FEDORA_IMAGE} \
    -t ${OPENJDK_IMAGE} \
    -f templates/${OPENJDK_TEMPLATE}.Dockerfile \
    . 1>&2

echo ${OPENJDK_IMAGE}
