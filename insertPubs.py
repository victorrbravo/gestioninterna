# -*- encoding: utf-8 -*-
import Safet
import os
import json
myhome = os.getenv("HOME")
mymedia = myhome + "/tmp"
myurl = "http://localhost"

print myhome
myinflow = Safet.MainWindow(myhome)

myinflow.setMediaPath(mymedia )
myinflow.setHostURL(myurl) 

myform = u"operacion:enviar_solicitud_por_correo Periodo_vacacional:86 Asunto:Planilla de vacaciones  Destinatarios: victorrbravo@gmail.com configurekey.Email/email.template.1: Se ha generado la planilla de vacaciones correspondiente al periodo solicitado <br/>. <br/> Estimado"
print myform

result = myinflow.login("vbravo","zpinquar") 

if not result:
	print "Authentication failed"
	exit()

result = myinflow.toInputForm(myform)


if not result:
	print "Form failed error: %s"  % (myinflow.currentError())
	exit()

myjson = u"%s" % (myinflow.currentJSON())
print myjson


