import re

def domain_name(url):
    patternn = r'^(?:https?://)?(?:www\.)?([^./:]+)'
    match = re.search(patternn,url)
    if match:
        return match.group(1)
    stripped = url.split('//')[-1]
    return stripped.split('.')[0]

tests = [
    ("http://github.com/carbonfive/raygun", "github"),
    ("http://www.zombie-bites.com", "zombie-bites"),
    ("https://www.cnet.com", "cnet"),
    ("www.xakep.ru", "xakep"),
    ("xakep.ru", "xakep"),
    ("http://blog.example.co.uk", "blog"),                  
    ("https://sub.domain.com/path", "sub"),              
]
for url, expected in tests:
    print(url, "->", domain_name(url), " expected:", expected)