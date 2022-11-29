# Call billing - Tính tiền điền thoại

- [1. Deploy](#1-deploy)

# 1. Deploy
```
$ docker-compose build
$ docker-compose up -d
$ docker-compose exec app sh
/code/user_portal # python manage.py migrate
/code/user_portal # python manage.py runserver 0.0.0.0:8000
