import re

def is_valid_phone_number(phone_number : str) -> bool :
    pattern = r'^(\+\d{1,3}[- ]?)?\d{10,12}$'
    return bool(re.match(pattern, phone_number))