
git clone https://github.com/AidarPutilov/Kurs6.git

cd Kurs6

Ввести настройки сервера PostgreSQL в файле config.py

sudo -i -u postgres
createdb kurs6aidar

poetry shell
poetry install

python3 manage.py migrate

python3 manage.py createusers

python3 manage.py runserver
