import re
from django.core.validators import ValidationError

def validate_phone_num(value):
    equal = re.match(r"^\+1?\d{9,15}$",value)
    if not equal:
        raise ValidationError('uygun deyil')
    return value