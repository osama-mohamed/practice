from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def validate_url(value):
    url_validator = URLValidator()

    reg_value = value
    if 'http' in reg_value:
        new_value = reg_value
    else:
        new_value = 'http://' + value
    try:
        url_validator(new_value)
    except:
        raise ValidationError('invalid URL syntax')
    return new_value


    # value_1_invalid = False
    # value_2_invalid = False
    # try:
    #     url_validator(value)
    # except:
    #     value_1_invalid = True
    # value_2_url = 'http://' + value
    # try:
    #     url_validator(value_2_url)
    # except:
    #     value_2_invalid = True
    # if value_1_invalid == False and value_2_invalid == False:
    #     raise ValidationError('invalid URL syntax')
    # return value




# def validate_url(value):
#     url_validator = URLValidator()
#     try:
#         url_validator(value)
#     except:
#         raise ValidationError('invalid URL syntax')
#     return value


def validate_domain(value):
    if not '.com' in value:
        raise ValidationError('invalid URL syntax because no .com in url')
    return value