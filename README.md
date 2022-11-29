# Опубликованное решение: https://qutoq.pythonanywhere.com/
Просмотр сформированных заказов доступен только из админ панели. По необходимости могу предоставить логин и пароль для ознакомления. 

# Локальный запуск:
```
git clone https://github.com/qutoq/django_stripe.git
```
Перейти в django_stripe/

В django_stripe/.env добавить свой stripe secret key без сохраненных промокодов в личном кабинете

По необходимости создайте виртуальное окружение и установите
```
pip install django 
pip install django-environ 
pip install stripe
```
Запуск локального сервера:

```
python manage.py migrate --run-syncdb
python manage.py createsuperuser
python manage.py runserver
```
Добавьте свои товары, скидки и налоги

# Выполненные дополнительные тестовые задания:
- Использование environment variables

- Просмотр Django Моделей в Django Admin панели

- Запуск приложения на удаленном сервере, доступном для тестирования

- Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items

- Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме. 

----------

+ От себя была реализована корзина через django sessions

# Возможные доработки
- В будущем, возможно, реализую webhook для подтверждения оплаты заказа
