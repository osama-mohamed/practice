from django.core.exceptions import ValidationError


BLOCKED_WORDS = ['cheap', 'bad']

def validate_blocked_words(value):
  init_value = str(value.lower())
  init_items = set(init_value.split())
  blocked = set([x.lower() for x in BLOCKED_WORDS])
  invalid_items = list(init_items.intersection(blocked))
  has_error = len(invalid_items) > 0
  if has_error:
    validatio_errors = []
    for i, invalid in enumerate(invalid_items):
      validatio_errors.append(ValidationError(f'\'{invalid}\' is a blocked word', params={'value': invalid}, code=f'blocked-woed-{i}'))
    raise ValidationError(validatio_errors)
  return value

validate_blocked_words('This is bad & cheap')