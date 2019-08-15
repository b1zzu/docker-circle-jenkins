#!/usr/bin/env bash

set -e
set -x

VERSION=${VERSION:-alpha}
NAMESPACE=${NAMESPACE:-}

GRADLE_VERSION=${1:-5.6}
OPENJDK_VERSION=${2:-8}
FEDORA_VERSION=${3:-31}

OPENJDK_IMAGE=$(./images/openjdk.sh ${OPENJDK_VERSION} ${FEDORA_VERSION})

GRADLE_IMAGE=${NAMESPACE}gradle:${VERSION}-fedora${FEDORA_VERSION}-openjdk${OPENJDK_VERSION}-gradle${GRADLE_VERSION}

docker build \
    --build-arg FROM=${OPENJDK_IMAGE} \
    --build-arg GRADLE_VERSION=${GRADLE_VERSION} \
    -t ${GRADLE_IMAGE} \
    -f templates/gradle.Dockerfile \
    . 1>&2

echo ${GRADLE_IMAGE}
