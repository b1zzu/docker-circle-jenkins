#!/usr/bin/env bash

set -e
set -x

FEDORA_VERSION=${1:-31}
FEDORA_IMAGE=b1zzu/fedora:${FEDORA_VERSION}

docker build \
    --build-arg VERSION=${FEDORA_VERSION} \
    -t ${FEDORA_IMAGE} \
    -f templates/fedora.Dockerfile \
    . 1>&2

echo ${FEDORA_IMAGE}
