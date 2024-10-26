# Hangman Game
http://hangmangame.pythonanywhere.com - sometimes loads on a 2nd time, server side issue

## Setup
There is no database needed so makemigrations and migrate are not needed but you may see some warning messages without doing that, which is fine as well.
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Go to provided link (http://127.0.0.1:8000/ by default)