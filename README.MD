install requirements: 
`pip install -r requirements.txt`

run migrations:
`python manage.py migrate`

load fixtures:
`django-admin loaddata app2/fixtures/language.json`
`django-admin loaddata app2/fixtures/country.json`

run project:
`python manage.py runserver`

run django-extensions console: 
`python manage.py shell_plus --ipython`

run in browser:
http://127.0.0.1:8000
