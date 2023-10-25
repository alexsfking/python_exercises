import re

# vague problem - assume subdomains ='www' for simplicity

pattern=re.compile(r"""
                   ^(?P<protocol>[a-zA-Z0-9-]+\:\/\/)?
                   (?P<subdomains>([w]+\.)*)?
                   (?P<domain>[a-zA-Z0-9-]+)
                   (?P<additional>(\.[a-zA-Z0-9-]+)+)
                   (?P<path>(\/[a-zA-Z0-9\-\.\_\~\:\/\?\#\[\]\@\!\$\&\'\(\)\*\+\,\;\=]+)+)?
                   (?P<trailing>\/)?$
                   """,re.VERBOSE)

def domain_name(url):
    match = pattern.match(url)
    return match.groupdict().get('domain')


print(domain_name("http://www.ukmwr.us"))
print(domain_name("https://dc0hryqroldx35r215h1iuy9.net/"))
print(domain_name("https://8fxqtw23zlyo9i0hss53h1g0o1.name/"))