# Call billing - Tính tiền điền thoại

- [1. Deploy](#1-deploy)

# 1. Deploy
```
$ docker-compose build
$ docker-compose up -d
$ docker-compose exec app sh
/code/ # python manage.py migrate
/code/ # python manage.py runserver 0.0.0.0:8000
/code/ # python manage.py createsuperuser
