#!/bin/bash

# Go to temp dir
cd "$2"
git clone "$1"

# check if Dockerfile exist
EXIST=0
if [ `find ./ -name "Dockerfile"` ]; then
  EXIST=1
fi

exit "$EXIST"

