# Recipe-App-API

# For Test
docker-compose run app sh -c 'python manage.py test && flake8'

# For Migrations
docker-compose run app sh -c 'python manage.py makemigrations && python manage.py migrate'

# Start server
docker-compose run app sh -c 'python manage.py runserver'

