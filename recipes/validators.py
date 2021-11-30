from django.core.exceptions import ValidationError

from pint import UnitRegistry
from pint.errors import UndefinedUnitError

vaild_units_measurements = ['pounds', 'lbs', 'oz', 'gram']

def validate_unit_of_measure(value):
  ureg = UnitRegistry()
  try:
    single_unit = ureg[value]
  except UndefinedUnitError as e:
    raise ValidationError(f"'{value}' is not a valid unit of measure")
  except:
    raise ValidationError(f"'{value}' is invalid. Unknown error.") 
  # if value not in vaild_units_measurements:
  #   raise ValidationError(f'{value} is not a valid unit of measure.')