import re

from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_username(value):
    if re.search(r'^[a-zA-Z][a-zA-Z0-9-_\.]{1,20}$', value) is None:
        raise ValidationError(
            (f'Не допустимые символы <{value}> в нике.'),
            params={'value': value},
        )
    if value == 'me':
        raise ValidationError(
            ('Имя пользователя не может быть <me>.'),
            params={'value': value},
        )


def validate_year(value):
    now_year = timezone.now().year
    if value > now_year:
        raise ValidationError(
            f'Нельзя добавить  произведение из будущего'
            f'Сейчас {now_year} год.')
    if value <= 0:
        raise ValidationError(
            'Год создания не может быть отрицательным')
