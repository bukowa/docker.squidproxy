FROM alpine@sha256:beefdbd8a1da6d2915566fde36db9db0b524eb737fc57cd1367effd16dc0d06d

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