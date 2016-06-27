#-*- coding: utf-8 -*-
import pika
import Safet
import re
import shutil
import os
import safetconfig
import sha
import random
import urllib, urllib2
import sys


from PyQt4.QtCore import *



def checkevents(req):
    myuser = "vbravo"
    mypass = "d91408cd"
	
    myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH) 
    myinflow.registerLogin(myuser)
    result = myinflow.login(myuser,mypass)
    if result == False:
		print "Fallo el acceso a la aplicacion"

    result = myinflow.checkAndExecEvents()
 	
    if result == True:
		print "Se ejecuto correctamente el chequeo de eventos programados - SAFET"
    else:
		print "NO se ejecuto el chequeo de eventos - SAFET" 

    return 

checkevents()

