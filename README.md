## Курсовая работа 6
- Реализован CRUD-механизм для управления рассылками, клиентами, сообщениями, блогами.
- Реализован скрипт рассылки, который работает как из командной строки, так и по расписанию.
- Реализован скрипт рассылки при запуске приложения.
- Реализован механизм авторизации и верификации пользователя, сброс пароля.
- Реализовано ограничение доступа к рассылкам для разных пользователей.
- Реализован интерфейс менеджера.



### Применённые пакеты
- django
- ipython
- pillow
- psycopg2-binary
- django-crispy-forms
- crispy-bootstrap5
- django-apscheduler
- redis
- python-dotenv

### Инструкция для развертывания проекта

#### Клонирование проекта:
git clone https://github.com/AidarPutilov/Kurs6.git

#### Переход в каталог
cd Kurs6

#### Базовые настройки
Ввести настройки сервера PostgreSQL в файле config.py

#### Создание базы данных
sudo -i -u postgres
createdb kurs6aidar

#### Активация Poetry, установка пакетов
poetry shell
poetry install

#### Применение миграций
python3 manage.py migrate

#### Создание пользователей, групп и разрешений
python3 manage.py createusers

#### Запуск проекта
python3 manage.py runserver

#### Запуск задач по расписанию
python3 manage.py runapscheduler

#### Запуск задач разово с учётом расписания
python3 manage.py runonce