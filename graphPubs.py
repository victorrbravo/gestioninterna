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


#myconsult = u"operacion:Generar_gráfico_con_autofiltro Cargar_archivo_flujo:/home/vbravo/.safet/flowfiles/tendencias_af.xml Autofiltro:por_sub"
#myconsult = u"operacion:Generar_gráfico_coloreado Cargar_archivo_flujo:/home/vbravo/.safet/flowfiles/estado_publicaciones.xml"
#myconsult = u"operacion:Generar_gráfico_coloreado Cargar_archivo_flujo:/home/vbravo/.safet/flowfiles/precio_publicaciones.xml parameters.BySearchWord:pendrive"
#myconsult = u"operacion:Generar_gráfico_con_autofiltro Cargar_archivo_flujo: /home/vbravo/.safet/flowfiles/dyn_precio_publicaciones.xml Autofiltro: por_ciudad parameters.BySearchWord:pendrive"
#myconsult = u"operacion:Generar_gráfico_con_autofiltro Cargar_archivo_flujo: /home/vbravo/.safet/flowfiles/dyn_precio_publicaciones.xml Autofiltro: por_ciudad parameters.BySearchWord:pendrive configurekey.Autofilter/autofilter.double.limit.last:30000"
#myconsult = u"operacion:Generar_gráfico_con_autofiltro Cargar_archivo_flujo: /home/vbravo/.safet/flowfiles/dyn_precio_publicaciones.xml Autofiltro: por_ciudad  configurekey.Plugins.Graphviz/plugins.graphviz.graph.rankdir:TB"

#myconsult = u"operacion:Listar_datos Cargar_archivo_flujo: /home/vbravo/.safet/flowfiles/order_precio_publicaciones.xml Variable: vTodas parameters.BySearchWord:pendrive"

#myconsult = u"operacion:Listar_datos_con_autofiltro Cargar_archivo_flujo: /home/vbravo/.safet/flowfiles/dyn_precio_publicaciones.xml Autofiltro: por_ciudad Variable:vTodas parameters.BySearchWord:pendrive"
#myconsult = u"operacion:Generar_gráfico_con_autofiltro Cargar_archivo_flujo: /home/vbravo/.safet/flowfiles/localidad_sub_publicaciones.xml Autofiltro: por_ciudad  parameters.BySearchWord:pendrive"

#myconsult = u"operacion:Generar_gráfico_con_autofiltro Cargar_archivo_flujo: /home/vbravo/.safet/flowfiles/localidad_marca_publicaciones.xml Autofiltro: por_ciudad  parameters.BySearchWord:laptop "

myconsult = u"operacion:Generar_gráfico_con_autofiltro Cargar_archivo_flujo: /home/vbravo/Filtros/localidad_publicaciones.xml Autofiltro:por_ciudad  parameters.BySearchWord:laptop"
#myconsult = u"operacion:Generar_gráfico_con_autofiltro Cargar_archivo_flujo: /home/vbravo/tmp/localidad_publicaciones.xml Autofiltro:por_ciudad  parameters.BySearchWord:laptop"

myconsult = u"operacion:Generar_gráfico_coloreado Cargar_archivo_flujo:/home/vbravo/.safet/flowfiles/SolicitudVistaVacacionesUser.xml"
#myconsult = u"operacion:Generar_gráfico_para_clave Clave: 65"
 

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




	 
