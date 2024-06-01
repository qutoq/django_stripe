## Старый сайт: https://qutoq.pythonanywhere.com/

Текущия версия с docker пока без хостинга

### Запуск:
```
git clone https://github.com/qutoq/django_stripe.git
```
Перейти в `django_stripe/`

Создайте `app/django_stripe/.env` по примеру `.env.example`


Запуск локального сервера по адресу `http://localhost:1337/`:

```
sudo docker-compose up --build
```
При первом запуске:
```
sudo bash migrate.sh 
```
```
sudo docker-compose exec web python manage.py createsuperuser
```

Теперь в `/admin' можно добавлять свои товары, скидки и налоги

Но! Для локального тестирования вебхука нужно
```
stripe login
stripe listen --forward-to localhost:1337/webhook
```

