#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
###################################################################
#
# Uebung:
# Lesen Sie die URL "http://www.digicomp.ch" ein
# Prüfen Sie, ob die Seite den Text "Hallo Python" beinhaltet
# Wenn ja, geben Sie den Text aus: "Seite ist ok"
# Ansonsten öffnen Sie die Seite direkt in Ihrem Browser
#
###################################################################

#### Lösung: ####

import webbrowser
import urllib

# URL einlesen
u = urllib.urlopen("http://www.digicomp.ch")
li = u.readlines()
u.close()

# Prüfe auf spezifischen Inhalt
e = "x"
for element in li:
    if b"Hallo Python" in element:
        e = "Seite ist ok"

if e == "x":
    webbrowser.open("http://www.digicomp.ch")
    #webbrowser.get(using='firefox').open("http://www.digicomp.ch")
else:
    print(e)
