# -*- coding: utf-8 -*-

import Safet
import os
import json
myhome = os.getenv("HOME")
mymedia = myhome + "/gits/gestioninterna/static/tmp"
myurl = "http://localhost"

myinflow = Safet.MainWindow(myhome)

myinflow.setMediaPath(mymedia )
myinflow.setHostURL(myurl) 


myconsult = u"operacion:Generar_gráfico_para_clave Clave: 190"
 

result = myinflow.login("vbravo","zpinquar") 

if not result:
      print "Authentication failed"
      exit()

result = myinflow.toInputConsole(myconsult)

if not result:
      print "Consult failed error: %s"  % (myinflow.currentError())
      exit()

myjson = u"%s" % (myinflow.currentJSON())
print myjson

#currjson  = json.loads(myjson)["safetlist"]

#if len(currjson)>0:
#      print currjson[0]["price_int"]




	 
