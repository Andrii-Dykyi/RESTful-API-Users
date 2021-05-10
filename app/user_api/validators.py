import re


def only_letters_validator(value):
    """
    Check if value consists only of letters.
    """
    return value.isalpha()


def phone_number_validator(value):
    """
    Validate phone number.
    """
    return re.fullmatch(r'\+380\d{9}', value)
