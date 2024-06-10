#!/bin/bash
set -e

tag=${DOCKER_TAG:-"squidproxy"}
push_tag=${DOCKER_PUSH_TAG:-"bukowa/squidproxy"}

if [[ "$1" == "build" ]]
then
  docker build --tag=$tag .
fi

if [[ "$1" == "copy" ]]
then
  docker run -d --name=$tag $tag
  docker cp $tag:/etc/squid/squid.conf .
  docker rm -f $tag
fi

if [[ "$1" == "attach" ]]
then
  docker run --rm -it -p 3128:3128 --entrypoint=/bin/bash $tag
fi

if [[ "$1" == "test" ]]
then
  set -x
  docker run --rm -it -p 3128:3128 \
    --name=$tag \
    -e SQUID_USER=DEFAULT_USER -e SQUID_PASS=DEFAULT_PASSWORD $tag
fi

if [[ "$1" == push ]]
then
  docker tag ${tag} ${push_tag}
  docker push ${push_tag}
fi

