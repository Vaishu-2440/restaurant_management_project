import re
from emails.utils import parseaddr

def is_valid_email(email : str) -> bool :
    if not email :
        return False

    parsed_email = parseaddr(email)[1]
    if not parsed_email :
        return False
    
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(email_regex, parsed_email) :
        return True
    return False

def is_valid_phone(phone : str) -> bool :
    if not phone :
        return False
    phone_regex = r"^\+?\d[\d-]{8,12}\d$"
    return bool(re.match(phone_regex, phone))