cd django/
echo DJANGO_APP
export DJANGO_SETTINGS='dev'
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py loaddata fixtures/data.json
python3 manage.py runserver
