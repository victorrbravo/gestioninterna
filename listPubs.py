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

#myconsult = u"operacion:Listar_datos Cargar_archivo_flujo: /home/vbravo/.safet/flowfiles/tendencias_sub.xml Variable: vPorCategoria"
#myconsult = u"operacion:Listar_datos Cargar_archivo_flujo: /home/vbravo/.safet/flowfiles/flujo_publicaciones.xml Variable: vDraft parameters.CurrPage: 0"
#myconsult = u"operacion:Listar_datos Cargar_archivo_flujo: /home/vbravo/.safet/flowfiles/flujo_publicaciones.xml Variable: vPublished parameters.CurrPage: 0"
#myconsult = u"operacion:Listar_datos Cargar_archivo_flujo: /home/vbravo/.safet/flowfiles/o_flujo_publicaciones.xml Variable: vDraft parameters.CurrPage: 0"
myconsult = u"operacion:Generar_gráfico_coloreado Cargar_archivo_flujo: /home/vbravo/.safet/flowfiles/flujogeneralsesiones.xml"
myconsult =u"operacion:Generar_gráfico_coloreado Cargar_archivo_flujo: /home/vbravo/.safet/flowfiles/flujo_publicaciones.xml"
myconsult = u"operacion:Listar_datos Cargar_archivo_flujo: /home/vbravo/.safet/flowfiles/SolicitudVistaVacaciones.xml Variable: vSolicitud parameters.ByPeriod:47"
print myconsult

result = myinflow.login("vbravo","zpinquar") 

if not result:
	print "Authentication failed"
	exit()

result = myinflow.toInputConsole(myconsult)


if not result:
	print "Consult failed error: %s"  % (myinflow.currentError())
	exit()

print myinflow.currentJSON()

exit()
mypubs = json.loads(u"%s" % (myinflow.currentJSON()) )["safetlist"]
print u"Result:\n"
print mypubs
for record in mypubs:
	#print record["orden"] + " " + record["id"] + " " +  record["owner"]
	print  record["id"] + " " +  record["owner"]
#	print record["summary"] + " "  +  record["owner"]


