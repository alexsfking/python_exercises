import re

camel_pattern=re.compile(r"^[a-z]+(?:[A-Z][a-z\d]*)*$")
snake_pattern=re.compile(r"^[a-z]+(?:\_[a-z]+)*$")
kebab_pattern=re.compile(r"^[a-z]+(?:\-[a-z]+)*$")

def change_case(identifier, target_case):
    match camel_pattern.match(identifier),