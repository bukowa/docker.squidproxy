## docker image for squidproxy

### Usage with basic http auth

```bash
docker run -d \
  -p 3128:3128 \
  --name squidproxy \
  -e SQUID_USER=admin \
  -e SQUID_PASS=admin \
  bukowa/squidproxy
```
![Docker Image Size](https://img.shields.io/docker/image-size/bukowa/squidproxy/latest)
![Docker Image Version](https://img.shields.io/docker/v/bukowa/squidproxy)
![Docker Pulls](https://img.shields.io/docker/pulls/bukowa/squidproxy)
1