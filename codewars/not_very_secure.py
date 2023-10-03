import re

valid_pattern = re.compile(r'^[0-9a-zA-Z]+$')

def alphanumeric(password):
    return bool(valid_pattern.match(password))