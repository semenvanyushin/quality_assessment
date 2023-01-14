### Описание:

Проект **api_yamdb** это бекэнд для сайта-агрегатора рецензий **YaMDb**, на котором вы можете посмотреть рейтинг интересующего вас произведения, написать о нем отзыв и поставить оценку, также вы можете комментировать чужие отзывы. 

 **api_yamdb** дает возможность передавать данные с помощью **REST API** интерфейса, доступные действия:

- регистрация пользоватея

- получение или обновление токена

- получение полного списка произведений

- посмотр уже имеющихся отзывов или добавление свого

- добавление комментария к другим отзывам

  и еще много всего.

  Полный список доступных эндпоинтов можно посмотреть здесь http://127.0.0.1:8000/redoc/, эта ссылка будет доступна после того как вы запустите проект, ниже описание того как это сделать. 

  *Замечание:* Для работы **redoc** необходимо в *settings.py* установить *DEBUG=True*

### Как запустить проект:

Клонируем репозиторий и переходим в него:
```bash
git clone https://github.com/semenvanyushin/infra_sp2.git
cd infra_sp2
cd api_yamdb
```

Создаем и активируем виртуальное окружение:
```bash
python3 -m venv venv
source /venv/bin/activate (source /venv/Scripts/activate - для Windows)
python -m pip install --upgrade pip
```

Ставим зависимости из requirements.txt:
```bash
pip install -r requirements.txt
```

Переходим в папку с файлом docker-compose.yaml:
```bash
cd infra
```

Поднимаем контейнеры (infra_db_1, infra_web_1, infra_nginx_1):
```bash
docker-compose up -d --build
```

Выполняем миграции:
```bash
docker-compose exec web python manage.py makemigrations reviews
```
```bash
docker-compose exec web python manage.py migrate
```

Создаем суперпользователя:
```bash
docker-compose exec web python manage.py createsuperuser
```

Србираем статику:
```bash
docker-compose exec web python manage.py collectstatic --no-input
```

Создаем дамп базы данных (нет в текущем репозитории):
```bash
docker-compose exec web python manage.py dumpdata > dumpPostrgeSQL.json
```

Останавливаем контейнеры:
```bash
docker-compose down -v
```

### Шаблон наполнения .env (не включен в текущий репозиторий) расположенный по пути infra/.env
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

#### Получить токен

```
POST http://127.0.0.1:8000/api/v1/auth/token/
Content-Type: application/json

{
    "username": "alena",
    "confirmation_code": "64u-188bc42c1126464cff29"
}
```

#### Добавить произведение( доступно только администраторам сайта)

```
POST http://127.0.0.1:8000/api/v1/titles/
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY1NDk1NjUxLCJpYXQiOjE2NjU0MDkyNTEsImp0aSI6IjkzMDI4Y2U2Yzc4MzQ4ZmRiMGQzYjAzMzdhOGU1NDhkIiwidXNlcl9pZCI6Mn0.Csq5sVXLhJTbYsZNdU7g5r2bRhsLXwtKchNUAmyi6uE
```

#### Посмотреть список всех произведений

```
http://127.0.0.1:8000/api/v1/titles/ 
```
![example workflow](https://github.com/semenvanyushin/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
