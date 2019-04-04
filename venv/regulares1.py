# -*- coding: utf-8 -*-
import re

txt="borja@hotmail.com"

if re.search("^[A-Z|a-z]+[@]+[A-Z|a-z]+[.]+[com|es]", txt):
    print "Correo válido"
else:
    print"Correo no válido"