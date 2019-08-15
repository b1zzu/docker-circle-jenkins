#!/usr/bin/env bash

set -e
set -x

VERSION=${VERSION:-alpha}
NAMESPACE=${NAMESPACE:-}

NODE_VERSION=${1:-10.16.2}
FEDORA_VERSION=${2:-31}

FEDORA_IMAGE=$(./images/fedora.sh ${FEDORA_VERSION})

NODE_IMAGE=${NAMESPACE}node:${VERSION}-fedora${FEDORA_VERSION}-node${NODE_VERSION}

docker build \
    --build-arg FROM=${FEDORA_IMAGE} \
    --build-arg NODE_VERSION=${NODE_VERSION} \
    -t ${NODE_IMAGE} \
    -f templates/node.Dockerfile \
    . 1>&2

echo ${NODE_IMAGE}
