import re

"""
You are given an integer  followed by  email addresses. Your task is to print
a list containing only valid email addresses in lexicographical order.

Valid email addresses must follow these rules:
    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores [a-z],[A-Z],[0-9],[_-].
    The website name can only have letters and digits [a-z],[A-Z],[0-9].
    The extension can only contain letters [a-z],[A-Z].
    The maximum length of the extension is 3.
"""

def fun(s):
    # return True if s is a valid email, else return False
    #example=r'username@websitename.extension'
    pattern='^[a-zA-Z0-9_\-]+[@][a-zA-Z0-9]+[\.][a-zA-Z]{1,3}$'
    prog = re.compile(pattern)
    result = prog.match(s)
    if(result):
        return True
    return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)