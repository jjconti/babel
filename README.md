# babel

Ejercicio de Django, DRF y bootstrap

## Cómo probarlo

$ git clone git@github.com:jjconti/babel.git

$ cd babel/

$ mkvirtualenv babel-dev

$ pip install -r requirements.txt

$ ./manage.py migrate

$ ./manage.py loaddata fixtures/contenttypes.json fixtures/auth.json fixtures/libros.json

$ ./manage.py runserver

Admin: http://127.0.0.1:8000/admin/ (admin/loscuerposdelverano)

API: http://127.0.0.1:8000/api/libros/

UI: http://127.0.0.1:8000/libros/
