```sh
docker run -d -p 6379:6379 --name redis --restart always redis:latest redis-server --requirepass kltn
```

### Setup .env

```sh
EMAIL_USER = ''
EMAIL_SERVER=''
PASSWORD=''
SMTP_SERVER=''
SMTP_PORT=
BROKER_URL=''
```

```sh
docker compose up --build -d
```