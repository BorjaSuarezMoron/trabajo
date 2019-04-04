import re

txt="https://www.example.com"
if re.search("^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+]$",txt):
    print "URL valida"
else:
    print "No valida"