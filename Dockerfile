FROM alpine@sha256:a8560b36e8b8210634f77d9f7f9efd7ffa463e380b75e2e74aff4511df3ef88c

LABEL org.opencontainers.image.source=https://github.com/bukowa/docker.squidproxy
LABEL org.opencontainers.image.licenses=MIT

RUN apk update
RUN apk add \
    apache2-utils \
    squid \
    bash

COPY squid.conf /etc/squid/squid.conf
EXPOSE 3128

COPY entrypoint.sh /sbin/entrypoint.sh
ENTRYPOINT ["/sbin/entrypoint.sh"]