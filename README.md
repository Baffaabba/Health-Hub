cd Health_hub
pip install django
pip install pillow

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver