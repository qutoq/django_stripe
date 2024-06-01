sudo docker-compose exec web python manage.py migrate --run-syncdb
sudo docker-compose exec web python manage.py collectstatic --no-input --clear
