#!/usr/bin/python3
##############################################
#
# Name: networker_uebung1.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 01.09.2022 1.0
#
# Purpose: Prüft die Antwort mehrerer IP-Adressen im Netz
#          und löst die Namen im DNS auf
#
##############################################

#Module
from os import system
from socket import gethostbyaddr

# Funktionen
def ping(adr):
   '''IP-Adresse im Netzwerk pingen'''

   response = system("ping -c 1 -t 2 " + adr + ">/dev/null 2>&1")
   return response

def get_name(adr):
   '''IP-Adresse im DNS auflösen'''

   try:
      ns=gethostbyaddr(adr)
      name=ns[0]
   except:
      name="unbekannt"
   return name

#Variabeln
adressen=['192.168.1.252','192.168.1.128','192.168.1.150','46.232.181.237']

#Main Script
for adr in adressen:
   response=ping(adr)
   name=get_name(adr)
   if response == 0 and name!='unbekannt':
      print (f"Host {adr} ist erreichbar und löst im DNS mit {name} auf")
   elif response == 0 and name=='unbekannt':
      print (f"Host {adr} ist erreichbar kann aber im DNS nicht aufgelöst werden")
   elif response != 0 and name!='unbekannt':
      print (f"Host {adr} ist nicht erreichbar kann aber im DNS mit {name} aufgelöst werden")
   else:
      print (f"Host {adr} ist nicht erreichbar und kann im DNS auch nicht aufgelöst werden")

