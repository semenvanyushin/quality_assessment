![Yamdb workflow](https://github.com/semenvanyushin/quality_assessment/actions/workflows/yamdb_workflow.yml/badge.svg)

### Описание:

Проект **quality_assessment** это бекэнд для сайта-агрегатора рецензий, на котором вы можете посмотреть рейтинг интересующего вас произведения, написать о нем отзыв и поставить оценку, также вы можете комментировать чужие отзывы. 

 **quality_assessment** дает возможность передавать данные с помощью **REST API** интерфейса, доступные действия:

- регистрация пользоватея

- получение или обновление токена

- получение полного списка произведений

- посмотр уже имеющихся отзывов или добавление свого

- добавление комментария к другим отзывам

  и еще много всего.

Стек:
- Django
- DRF
- djangorestframework-simplejwt
- psycopg2-binary
- PyJWT

### Как запустить проект:

Клонируем репозиторий и переходим в него:
```bash
git clone https://github.com/semenvanyushin/quality_assessment.git
cd yamdb_final
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
