from django.core.exceptions import ValidationError

def validate_even(value):
  if value % 2 != 0:
    raise ValidationError(
      '%(value)s is not an even number',
      params={'value':value},  
    )

def validate_name(value):
  name = value
  if name == "":
     raise ValidationError("Name must be complete")

