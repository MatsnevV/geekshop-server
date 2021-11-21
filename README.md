
$venv\Scripts\activate.bat

$(venv) pip freeze > requirements.txt

$(venv) pip install -r requirements.txt

$ python  manage.py runserver

$
$
$
$
$
$
$

source venv/bin/activate
cd geekshop/
python3  manage.py runserver
