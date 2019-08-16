#!/usr/bin/env bash

NAMESPACE="b1zzu"

OPTIONS="-n ${NAMESPACE}"

if [ ! -z "$CIRCLE_TAG" ]; then
    OPTIONS="$OPTIONS -v $CIRCLE_TAG -p"
fi

exec ./build.py $OPTIONS $@
