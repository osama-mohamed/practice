from django.core.exceptions import ValidationError


CATEGORIES = ['a', 'b', 'c', 'd']


def validate_category(value):
    if not value in CATEGORIES:
        raise ValidationError('{} not valid category!'.format(value))
        # raise ValidationError(f'{value} not valid category!')
