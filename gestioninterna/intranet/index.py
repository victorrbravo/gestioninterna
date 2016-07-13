#-*- coding: utf-8 -*-
from mod_python import apache
from mod_python import util
from mod_python import Session
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
import json 

#from safetconfig import *

from PyQt4.QtCore import *

myglobal = None




def handler(req):
    selurl = u"%s" % ( req.parsed_uri[apache.URI_PATH].decode("utf-8"))
    print "*" * 80
    print "entering..."
    #print u"entering..." + selurl

    print "*" * 80
    resultstr = u""
    if selurl[-1] == "/":
	selurl = selurl[0:len(selurl)-1]

    if not selurl.endswith("complete"):
	    req.content_type = "text/html; charset=ISO-8859-1"
	    req.send_http_header()
    else:
	    req.content_type = "text/plain; charset=ISO-8859-1"
	    req.send_http_header()

    if selurl.endswith("/intranet"):
	resultstr = safetprincipal(req)
    elif selurl.endswith("/login"):
        resultstr = safetlogin(req)
    elif selurl.endswith("/createbdoc"):
        resultstr = safetcreatebdoc(req,selurl)
    elif selurl.endswith("/goregister"):
        resultstr = safetgoregister(req)   
    elif selurl.endswith("/goresendpassword"):
        resultstr = safetgoresendpassword(req)   
    elif selurl.endswith("/resendpassword"):
        resultstr = safetresendpassword(req)    
    elif selurl.find("/gochangepassword") != -1:
        resultstr = safetgochangepassword(req,selurl)     
    elif selurl.endswith("/changepassword"):
        resultstr = safetchangepassword(req)    
    elif selurl.find("/activeaccount/") != -1:
        resultstr = safetactiveaccount(req,selurl)     
    elif selurl.endswith("/changerole"):
        resultstr = safetchangerole(req)
    elif selurl.endswith("/register"):
        resultstr = safetregister(req)
    elif selurl.endswith("/finalizebdoc"):
        resultstr = safetfinalizebdoc(req,selurl)
    elif selurl.endswith("/gologin"):
	resultstr = safetgologin(req)
    elif selurl.endswith("/logout"):
	resultstr = safetlogout(req)	
    elif selurl.endswith("/goquickconsole"):
	resultstr = safetgoinputconsole(req)
    elif selurl.endswith("/goinputform"):
	resultstr = safetgoinputform(req)
    elif selurl.endswith("/goinputconsole"):
	resultstr = safetgoinputconsolemenu(req)
    elif selurl.endswith("/1"):
	resultstr = safetinsert(req)
    elif selurl.endswith("/2"):
	resultstr = safetconsole(req,selurl)
    elif selurl.endswith("conscomplete"):
	resultstr = safetconsautocomplete(req)
    elif selurl.endswith("formcomplete"):	
	resultstr = safetformautocomplete(req)
    elif selurl.endswith("loaddata"):	
	resultstr = safetloaddata(req)
    elif selurl.endswith("savegraph"):	
	resultstr = safetsavegraph(req)
    elif selurl.endswith("viewtable"):	
	resultstr = safetviewtable(req)
    elif selurl.endswith("loadpars"):	
	resultstr = safetloadpars(req)
    elif selurl.endswith("/goabout"):	
	resultstr = safetgoabout(req)
    elif selurl.endswith("consola:Editar_grafo"):	
	resultstr = safetgoeditor(req)
    elif selurl.endswith("consola:Guardar_grafo") or selurl.endswith("/save"):	
	resultstr = safetsaveeditor(req)
    elif selurl.find("/api/") != -1:	
	resultstr = safetprocessapi(req,selurl)
    elif selurl.find("deftrac:operacion:") != -1:
	print "debug deftrac" 
	resultstr = safetgenerateform(req,selurl)
    elif selurl.find("defconsole:operacion:") != -1:
	resultstr = safetgenerateconsole(req,selurl)
    elif selurl.find("forma:") != -1:
	resultstr = safetprocessform(req,selurl)
    elif selurl.find("consola:") != -1:
	print "debug consola"
	resultstr = safetprocessconsole(req,selurl)
    elif selurl.find("flujo:") != -1:
        resultstr = safetgenerarflujo(req,selurl)


    resultstr = resultstr.encode("latin_1")

    req.write(resultstr)
    return apache.OK

def safetloadpars(req):
	form = util.FieldStorage(req,keep_blank_values=1)
		
	resultstr = u""
	sess = Session.Session(req,timeout=60*60)
	if not sess.has_key("inflow"):
        	return u"No se iniciado la sesión"
	if not sess['inflow']:
        	return u'No se ha autenticado. Siga este <a href="%s">enlace</a>  para autenticarse' % (safetconfig.LOGIN_URL)


    	myflowname  =u"%s".strip()  % (form.get("primary",None).decode("utf-8") )
	if ( len(myflowname) == 0 ):
		return "SafetErrorFaltanDatos"

	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
	result = myinflow.login(sess['user'],sess['pass'])
	if not result:
		return u"Error en la autenticación"

	resultstr = u"%s" % (myinflow.getFlowParameters(myflowname))
	return resultstr

def safetsavegraph(req):

	form = util.FieldStorage(req,keep_blank_values=1)

	sess = Session.Session(req,timeout=60*60)
	resultstr = safettests(sess)
	if len(resultstr) > 0:
		return resultstr
	
	mypars = QStringList()
	graphname = form.get("gname",None).decode("latin_1").strip()
	mypars.append(graphname)

	if sess.has_key("codegraph"):
		mypars.append(sess["codegraph"])
	if sess.has_key("dategraph"):
		mypars.append(sess["dategraph"])
	if sess.has_key("firstvalue"):
		mypars.append(sess["firstvalue"])
      
	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
	result = myinflow.login(sess['user'],sess['pass'])
	if not result:
		resultstr = "Error en la autenticación" 
	else:
		result = myinflow.doSaveGraph(mypars)		
		if result:
	        	resultstr = u"¡Grafo guardado exitosamente!"
		else:
			resultstr = u"El Grafo NO fue guardado"

	return resultstr

def safetviewtable(req):

#	form = util.FieldStorage(req,keep_blank_values=1)

	sess = Session.Session(req,timeout=60*60)
	resultstr = safettests(sess)
	if len(resultstr) > 0:
		return resultstr
	
	mytable = u"no hay currenttable"
	if sess.has_key("currenttable"):
		mytable = sess["currenttable"]

	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
	result = myinflow.login(sess['user'],sess['pass'])
	if not result:
		resultstr = u"Error en la autenticación" 
	else:
		resultstr = u"%s" % (mytable)

	return resultstr



def safetfinalizebdoc(req,selurl):
	if myglobal != None:
		return u"Inflow is alive!"
	return u"myinflowb is None"


def  safetprocessapi(req,selurl):
	result = "Hola: %s<br/>" % (selurl)

	form = util.FieldStorage(req,keep_blank_values=1)
	fields = {}
	myticket = selurl.rpartition('/')[-1]

	result = result + myticket + "<br/>"
	currentapp = safetconfig.HOMESAFET_PATH
	typeaction = "input"

	for k in form.keys():
		newk = k
		newvalue = form.get(newk,"")
		result = result + u"[%s] = %s<br/>" % (newk.decode("latin_1"),newvalue.decode("latin_1"))
		fields[newk] = newvalue
		
	result = result + "-----------------<br/>";
	result = result + "fields[%s] = %s<br/>" % ("accion",fields["accion"].decode("latin_1"))

	if not fields.has_key("accion"):
		return u"Error: de formación de URL"
	if fields.has_key("tipoaccion"):
		typeaction = fields["tipoaccion"]
	if fields.has_key("aplicacion"):
		currentapp = "/home/%s" % (fields["aplicacion"])

	myinflow = Safet.MainWindow(currentapp)
    	myinflow.setMediaPath(safetconfig.MEDIA_PATH)
	myinflow.setHostURL(safetconfig.SERVER_URL)     
	myinflow.log("selurl %s" % (selurl) )

	islogin = myinflow.login(myticket,"")
	if not islogin:
		return u"Error: en la autenticación"

	myinflow.log("typeaction console CONSOLE typeaction:%s" % (typeaction))
	myinflow.log("typeaction console CONSOLE aplicacion:%s" % (currentapp))

	myoperation = fields["accion"]

	if typeaction == "console":
		myinflow.log("typeaction console CONSOLE operation:%s" % (myoperation))
		isinserted = myinflow.toInputConsole( myoperation )

		if isinserted:
			myjson = myinflow.currentJSON()
			myfile = ""
			try:
				myfile = json.loads(myjson)["filename"]
			except:
				myfile = myjson
				print "es un reporte"
			return u"%s" % (myfile)
		else:
			return u"%s" % (myinflow.currentError())

	else:  
		isinserted = myinflow.toInputForm(myoperation )
		myinflow.log("RESULTAPI: %s" % (result) )
		if isinserted == "Ok":		
			result = u"<p align=center>Se realizó la operación <b>correctamente</b>.</p>"
		elif len(isinserted) > 0:
			result = u"<br/>Mensaje:%s" % (isinserted)
		else:

			result = u"<br/>Error:%s" % (isinserted)
	return result



def safetcreatebdoc(req,selurl):


	form = util.FieldStorage(req,keep_blank_values=1)
	print "...entrando a safetcreatebdoc......"		
	resultstr = u""
	sess = Session.Session(req,timeout=60*60)
	if not sess.has_key("inflow"):
        	return u"No se iniciado la sesión"
	if not sess['inflow']:
        	return u'No se ha autenticado. Siga este <a href="%s">enlace</a>  para autenticarse' % (safetconfig.LOGIN_URL)

	currerror = ""
	myglobal = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
	result = myglobal.login(sess['user'],sess['pass'])
	if not result:
		return u"Error en la autenticación"

	result = myglobal.createBdoc("algo")

	if result:
		return u"Fue Creado (createBdoc)"



def myfunc(myuser,mypass,mypost):
	currerror = ""
	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
	result = myinflow.login(myuser,mypass)
	myinflow.log("myfunc")
	isinserted = myinflow.toInputForm(mypost )



def safetprocessform(req,selurl):
	form = util.FieldStorage(req,keep_blank_values=1)
		
	resultstr = u""
	sess = Session.Session(req,timeout=60*60)
	if not sess.has_key("inflow"):
        	return u"No se iniciado la sesión"
	if not sess['inflow']:
        	return u'No se ha autenticado. Siga este <a href="%s">enlace</a>  para autenticarse' % (safetconfig.LOGIN_URL)

	currerror = ""
	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
	result = myinflow.login(sess['user'],sess['pass'])
	if not result:
		return u"Error en la autenticación"

	myoperation = u"%s" % ( selurl.rpartition("/")[2].replace("forma","operacion") + " ")
	myfields = u""


	myinflow.log("..........Viendo las claves que pasan.....")

	conffields = {}
	confvalue = ""
	confk = ""

	for k in form.keys():
		if not k.startswith("safet") :
			newk = k

			newvalue = form.get(newk,"")
			strtype = "%s" % type(newvalue)
			myinflow.log("strtype: |%s|" % (strtype))

			if strtype == "<type 'list'>": 
				newvalue =  newvalue[1]
				strtype = "%s" % type(newvalue)
				myinflow.log("............VERLISTA....................Nuevo strtype: |%s|" % strtype )
			if strtype == "<type 'instance'>":			
				myinflow.log("newvalue 1")
				fileitem = newvalue
				dir_path = safetconfig.MEDIA_PATH
				dir_url  = safetconfig.MEDIA_URL
				if fileitem.filename == "":
					continue
				myurl = dir_url + "/" + fileitem.filename
				myname = os.path.join(dir_path, fileitem.filename)
				
				open(myname, 'wb').write(fileitem.file.read())
				newvalue = myurl
				myinflow.log("newvalue 2: %s" % newvalue)
				
			else:
				newvalue = form.get(newk,"").decode("latin_1").strip()
				#myinflow.log("newk: %s newvalue: %s" % (newk, newvalue))


			newvalue = newvalue.replace(":","##SAFETCOLON##")
			newvalue = newvalue.replace(",","##SAFETCOMMA##")
			if len(newvalue) > 0:
				newitem = u" %s: %s\n" % (newk.decode("latin_1"), newvalue) 
				myfields =  u"%s" %(newitem) + myfields


	myoperation = myoperation + myfields
#	if True:
#		return myoperation
        
	isinserted = myinflow.toInputForm(myoperation )
	if isinserted == "Ok":
		resultstr = resultstr + u"<div class=\"success\">Se realizó la  operación <b>correctamente!</b></div>"
		allpost = "%s".strip() %  (myinflow.postAction()) 
	        postlist = allpost.split("##SAFETSEPARATOR##")
		if len(allpost)>0 and len(postlist) > 0:
			myinflow.log("Hay acciones posteriores")
			for mypost in postlist:
				if mypost.find("Generar_ticket") >= 0:
					myinflow.log("  EJECUTANDO (USER) POSTACTION: %s" % (mypost))
					isinserted = myinflow.toInputUsers(mypost)	
				else:
					myinflow.log("  EJECUTANDO (FORM) POSTACTION: %s" % (mypost))
					isinserted = myinflow.toInputForm(mypost,False)	
				myinflow.log("EJECUTADA")		

			resultstr = resultstr + u"<br/><div class=\"success\">Se ha enviado un correo a su cuenta, donde podrà bajar e imprimir el documento (planilla)</b></div>"
#			connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
#			channel = connection.channel()
#			channel.queue_declare(queue='hello')
#			message = mypost
#			channel.basic_publish(exchange='',routing_key='hello',body=message)
#			myinflow.log("Hay acciones posteriores pika (2)")

	elif len(isinserted) >  0:
		resultstr = isinserted
		myinflow.log(u"FROM INDEX.PY toInputForm resultstr:|%s|" % (resultstr) )
	        myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
		myinflow.setHostURL(safetconfig.SERVER_URL)     
        	resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr,safetconfig.TEMPLATES[13]))
		return resultstr
	else:
		resultstr = resultstr + u"<div class=\"error\">La operación  <b>NO</b> fue realizada.<br/>"
		myerror = myinflow.currentError().toLatin1().data()
		resultstr = resultstr +  u"El error fue el siguiente:<br/>%s</div>" % ( myerror.decode("latin_1"))


        resultstr = resultstr + u"<br/> <a href=\"%s\">Regresar al Formulario</b></a>" % (selurl.replace("forma:","deftrac:operacion:"))
        myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
	myinflow.setHostURL(safetconfig.SERVER_URL)     
        resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr,safetconfig.TEMPLATES[15]))

	return resultstr 

def safetprocessconsole(req,selurl):
	print "safet process console"
	print "*" * 80
	form = util.FieldStorage(req,keep_blank_values=1)
		
	resultstr = u""
	sess = Session.Session(req,timeout=60*60)
	if not sess.has_key("inflow"):
        	return u"No se iniciado la sesión"
	if not sess['inflow']:
        	return u'No se ha autenticado. Siga este <a href="%s">enlace</a>  para autenticarse' % (safetconfig.LOGIN_URL)

	currerror = ""
	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
    	myinflow.setMediaPath(safetconfig.MEDIA_PATH)
	myinflow.setHostURL(safetconfig.SERVER_URL)     
	result = myinflow.login(sess['user'],sess['pass'])
	if not result:
		return u"Error en la autenticación"

	myoperation = selurl.rpartition("/")[2].replace("consola","operacion") + " "
	nameoperation = myoperation
	myfields = u""
	print "myoperation**"

	confk = u""
	confvalue = u""
	conffields = {}
	parsk = u""
	parsvalue = u""
	parsfields = {}
	firstvalue = ""
        currentpar = ""
	for k in form.keys():
		if k.startswith("configurekey."):
			confk = k.decode("latin_1")
			confvalue = form.get(confk,"").decode("latin_1").strip()
			confk = confk[len("configurekey."):]
			if len(confvalue) > 0:
				conffields[confk] = confvalue	
		elif k.startswith("parameters."):
			parsk = k.decode("latin_1")
			parsvalue = form.get(parsk,"").decode("latin_1").strip()
			currentpar = parsk + ":" + parsvalue
			parsk = parsk[len("parameters."):]
			if len(parsvalue) > 0:
				parsfields[parsk] = parsvalue
		elif not k.startswith("safet") :
			newk = k.decode("latin_1")
			newvalue = form.get(newk,"").decode("latin_1").strip()
			if len(newvalue) > 0:
				newitem = u" %s: %s\n" % (newk, newvalue.replace(":","##SAFETCOLON##").replace(",","##SAFETCOMMA##") ) 
				myfields =  unicode(newitem) + myfields
				if len(firstvalue) == 0:
					firstvalue = newvalue
	
	if not conffields.has_key("GeneralOptions/generaloptions.currentflowtitle"): 
	      conffields["GeneralOptions/generaloptions.currentflowtitle"] = firstvalue

	myinflow.setConffileValues(conffields)
	myinflow.setParsValues(parsfields)
	myoperation = myoperation + myfields
        os.putenv("GV_FILE_PATH","/var/www/media") 
	print "myoperation process console"
	print "*" * 80
	#print myoperation
	print "*" * 80
 
	isgood = myinflow.toInputConsole(myoperation)
	currtemplate = safetconfig.TEMPLATES[2]
	response = ""
	if isgood:
		response  = u"%s" % (myinflow.currentJSON())
		try:
			response = json.loads(response)["filename"]
		except:
			print "Es un reporte" 

		if response.endswith(".png"):	
			resultstr = u"""
<html>
<head>
			"""

			mytitle = myinflow.currentGraphTitle();
			if mytitle.count()>0:
				resultstr = resultstr + "<title>%s</title>" % (mytitle)
			else:
				resultstr = resultstr + "<title>%s</title>" % ("Sistema Automatizado para la Firma y Estampillado de Tiempo - SAFET")
		
			resultstr = resultstr + """
</head>
<body>
			"""
			if mytitle.count() > 0:	
				resultstr = resultstr +u"<h2>%s</h2></br>" % (mytitle)
			myts = myinflow.addInfoGraphDateText()
			if myts.count() > 0:
				resultstr = resultstr +u"<b>%s</b></br>" % (myts)
			resultstr = resultstr + u"<div align=\"center\"><img src=\"%s/%s\"></img></div>" % (safetconfig.MEDIA_URL,response)

		elif response.find(".svg") > 0:

			resultstr = u""
#			mydata  =  json.loads(response)
#			response = mydata["filename"]
#			response = mydata
			mytitle = myinflow.currentGraphTitle()
#			mytitle = response
			if mytitle.count()>0:
				resultstr = resultstr + "<title>%s</title>" % (mytitle)
			else:
				resultstr = resultstr + "<title>%s</title>" % ("Sistema Automatizado para la Firma y Estampillado de Tiempo - SAFET")
			resultstr = resultstr + safetconfig.JS_SAFETPROCESSCONSOLE_HEAD
                         
                        resultstr = resultstr + " var svg = $('#svgload').svg({loadURL: '%s/%s',onLoad: null, settings: {changeSize: false} });" % (safetconfig.MEDIA_URL,response)
		        resultstr = resultstr + safetconfig.JS_SAFETPROCESSCONSOLE_FUNCTIONS
		        
			if mytitle.count() > 0:	
				resultstr = resultstr +u"<h2>%s</h2></br>" % (mytitle)
		        myts = myinflow.addInfoGraphDateText()
			if myts.count() > 0:
				resultstr = resultstr +u"<b>%s</b></br>" % (myts)
		        resultstr = resultstr + safetconfig.JS_SAFETPROCESSCONSOLE_BOTTOM

		elif response.endswith("##SAFETMESSAGE##"):
			response = response.replace("##SAFETMESSAGE##","")
			currtemplate = safetconfig.TEMPLATES[15]
		        myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
              		response = response + u"<br/> <a href=\"%s\">Regresar a la Consulta</b></a>" % (selurl.replace("consola:","defconsole:operacion:")) 
			resultstr = u"%s" % (myinflow.loadReportTemplate("<div class=\"success\">"+response+"</div>",currtemplate))

			return resultstr
		else:			
			if nameoperation.strip().endswith("consolidado"):			
				currtemplate = safetconfig.TEMPLATES[12]
			elif nameoperation.strip().endswith("general"):
#				currtemplate = safetconfig.TEMPLATES[16]
				currtemplate = ""
			else:
				currtemplate = safetconfig.TEMPLATES[3]
		        myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
			#response = response + u"<br/> <a href=\"%s\">Regresar a la Consulta</b></a>" % (selurl.replace("consola:","defconsole:operacion:"))			 
		        resultstr = u"%s" % (myinflow.loadReportTemplate(response,currtemplate,selurl))
			return resultstr
	else:
		resultstr = resultstr + u"<div class=\"error\">La operación  <b>NO</b> se realizó.<br/>"
		myerror = myinflow.currentJSON().toLatin1().data()
		resultstr = resultstr +  u"El error fue el siguiente:<br/>%s</div>" % ( myerror.decode("latin_1"))

	mylist = myinflow.lastInfoGraph()
	sess['codegraph'] = mylist[0]
	sess['dategraph'] = mylist[1]
        sess['firstvalue'] = myfields
	sess['currenttable'] = myinflow.currentTable()

	sess.save()
#        resultstr = resultstr + u"<br/> <a href=\"%s\">Regresar a la Consulta</b></a>|  <a href=\"#\" id=\"savegraphbutton\" name=\"savetgraphbutton\" onClick=\"jsSaveGraph('%s')\">Guardar Grafo</a> | <a href=\"%s/%s\">Bajar archivo SVG</a> | <a href=\"#\" id=\"viewtable\"  name=\"viewtable\" onClick=\"jsViewTable('%s')\" >Ver actividades</a>" % (selurl.replace("consola:","defconsole:operacion:"),myinflow.hostURL(),safetconfig.MEDIA_URL,response,myinflow.hostURL()+"/viewtable")
        resultstr = resultstr + u"<br/> <a href=\"%s\">Regresar a la Consulta</b></a>|  <a href=\"#\" id=\"savegraphbutton\" name=\"savetgraphbutton\" onClick=\"jsSaveGraph('%s')\">Guardar Grafo</a> | <a href=\"%s/%s\">Bajar archivo SVG</a>" % (selurl.replace("consola:","defconsole:operacion:"),myinflow.hostURL(),safetconfig.MEDIA_URL,response)

	resultstr = resultstr + ""
        myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
	myinflow.setHostURL(safetconfig.SERVER_URL)     
        resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr,currtemplate))
 
	return resultstr 

def safetconsautocomplete(req):
	form = util.FieldStorage(req,keep_blank_values=1)
	myq = unicode(form.get("q",None)).strip().lower()
		
	resultstr = u""
	sess = Session.Session(req,timeout=60*60)
	if not sess.has_key("inflow"):
        	return u"No se iniciado la sesión"
	if not sess['inflow']:
        	return u'No se ha autenticado. Siga este <a href="%s">enlace</a>  para autenticarse' % (safetconfig.LOGIN_URL)

	currerror = ""
	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
	result = myinflow.login(sess['user'],sess['pass'])
	if not result:
		return u"Error en la validación"
	mylist = myinflow.autoComplete(safetconfig.HOMESAFET_PATH + "/.safet/input/defconsole.xml")
	mydict = myinflow.loadEditActions()

	for k in mydict.keys():
		nstr = unicode(k).lower()
		if nstr.find(myq) != -1:
			newstr = "%s|%s\n" % (k,mydict[k])
			resultstr = resultstr + newstr
		

	return resultstr

def safetformautocomplete(req):
	form = util.FieldStorage(req,keep_blank_values=1)
	myq = unicode(form.get("q",None)).strip().lower()
		
	resultstr = u""
	sess = Session.Session(req,timeout=60*60)
	if not sess.has_key("inflow"):
        	return u"No se iniciado la sesión"
	if not sess['inflow']:
        	return u'No se ha autenticado. Siga este <a href="%s">enlace</a>  para autenticarse' % (safetconfig.LOGIN_URL)
	currerror = ""
	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
	result = myinflow.login(sess['user'],sess['pass'])
	if not result:
		return u"Error en la validación"
	mylist = myinflow.autoComplete(safetconfig.HOMESAFET_PATH + "/.safet/input/deftrac.xml")
	for n in mylist:
		nstr = unicode(n).lower()
		if nstr.find(myq) != -1:
			newstr = "%s\n" % (n)	
			resultstr = resultstr + newstr


	return resultstr

def safetprincipal(req):
	sess = Session.Session(req,timeout=60*60)
	#resultstr = u'<p align="center"><a href="http://localhost/intranet/login"> Entrar a <b>SAFET - Intranet</b></a><br/></p><br/>'
	resultstr = u'<p align="center"><a href="%s"> Entrar a <b>SAFET - Gestión</b></a><br/></p><br/>'% (safetconfig.LOGIN_URL)
	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH )
        #myinflow.setTemplatePath("http://localhost/media/templates/")
        myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
	#myinflow.setHostURL("http://localhost/intranet")     
	myinflow.setHostURL(safetconfig.SERVER_URL)     
	#resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr,u"/var/www/media/templates/index.html"))
        resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr,safetconfig.TEMPLATES[0]))
	return resultstr



def safetlogout(req):
	sess = Session.Session(req,timeout=60*60)
	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)

    	if sess.has_key("user"):
		myinflow.registerLogout(sess['user'])
		sess.delete()
		sess.cleanup()
	else:
		myinflow.log(u"Ha expirado el tiempo de sesión (logout)....<p align=""center""><a href=""%s""> Entrar a <b>SAFET</b></a><br/></p><br/>" % (safetconfig.LOGIN_URL))
		return
	resultstr =  u"Saliendo de la sesión...ok<p align=""center""><a href=""%s""> Entrar a <b>SAFET</b></a><br/></p><br/>" % (safetconfig.LOGIN_URL)
	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
        myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
	myinflow.setHostURL(safetconfig.SERVER_URL)     
        resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr,safetconfig.TEMPLATES[0]))
	return resultstr

def safetgoabout(req):
	sess = Session.Session(req,timeout=60*60)
	resultstr =  safetconfig.SAFETGOABOUT

	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
        myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
	myinflow.setHostURL(safetconfig.SERVER_URL)     
        resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr, safetconfig.TEMPLATES[10]))
	return resultstr


def safetlogin(req):
    generalform = safetconfig.SAFETLOGIN

    resultstr = u""
    sess = Session.Session(req,timeout=60*60)
    isauth = False
    myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
    myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
    myinflow.setHostURL(safetconfig.SERVER_URL)     
 
    currtemplate = safetconfig.TEMPLATES[9]
    if not sess.has_key("inflow"):
	sess['inflow'] = False
	sess.save()
	currtemplate =  safetconfig.TEMPLATES[9]
    else:
	if sess["inflow"]: 
	    	generalform = u"Ya está autenticado con el usuario <b>%s</b>" % (sess['user'])
		currtemplate =  safetconfig.TEMPLATES[11]
    
    resultstr = u"%s" % (myinflow.loadReportTemplate(generalform,currtemplate))
    return resultstr


def printlinks():
	result = safetconfig.PRINTLINKS
	return result


def safetregister(req):
    sess = Session.Session(req,timeout=60*60)
    currerror =  ""
    myuser = None
    mypass = None
    form = util.FieldStorage(req,keep_blank_values=1)
    myaccount = form.get("account",None)

    myfullname = u"%s" %  ( form.get("fullname",None).decode("latin_1"))
    myemail = form.get("email",None)
    myone = form.get("passwordone",None)
    mytwo = form.get("passwordtwo",None)
    mychallenge = form.get("recaptcha_challenge_field",None)
    myresponse = form.get("recaptcha_response_field",None)

 


    myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH) 
    if myuser != None:	
	    myinflow.registerLogin(myuser)
	    result = myinflow.login(myuser,mypass)

    resultstr = u""

    #if mychallenge == myresponse:
#	resultstr = u"%s" % ("No coincide el texto con la imagen (captcha)")
 #   else:
    resultstr = u"%s" % (myinflow.checkUserRegister(myfullname,myaccount,myemail,myone,mytwo)) 



    myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
    myinflow.setHostURL(safetconfig.SERVER_URL)     
    resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr, safetconfig.TEMPLATES[14]))
    return resultstr

def safetgochangepassword(req,selurl):
    sess = Session.Session(req,timeout=60*60)
    currerror =  ""
    form = util.FieldStorage(req,keep_blank_values=1)
    myuser = None
    mypass = None

    mykey = selurl.rpartition("/")[2]
    myaccount = mykey.partition("_")[0]



    myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH) 
    myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
    myinflow.setHostURL(safetconfig.SERVER_URL)    

    mylist = myinflow.getInfoOfUser(myaccount)
    if len(mylist) == 0:
	 return u"%s" % (myinflow.loadReportTemplate(u"No se encuentra el nombre de cuenta (%s) en la lista de usuarios" % (myaccount), safetconfig.TEMPLATES[14]))


    mycheck1 = unicode(mylist[0]).rpartition("_")[0]
    mynewpass = "_"+unicode(mylist[0]).rpartition("_")[2]
    mycheck2 = "_"+mykey

    resultstr = u"El código de activación de cuenta no es correcto. Verifique el enlace suministrado"
    if mycheck1 == mycheck2:
    	resultstr = u""
	resultstr = safetconfig.SAFETCHANGEPASSWORD % (myaccount)
    else:
	resultstr = u"No coindice los datos para reiniciar la contraseña"


 
    resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr, safetconfig.TEMPLATES[14]))
    return resultstr




def safetactiveaccount(req,selurl):
    sess = Session.Session(req,timeout=60*60)
    currerror =  ""
    myuser = None
    mypass = None
    form = util.FieldStorage(req,keep_blank_values=1)


    mykey = selurl.rpartition("/")[2]
    myaccount = mykey.partition("_")[0]

    myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
    myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
    myinflow.setHostURL(safetconfig.SERVER_URL)     

    mylist = myinflow.getInfoOfUser(myaccount)
    if len(mylist) == 0:
	 return u"%s" % (myinflow.loadReportTemplate(u"No se encuentra el nombre de cuenta (%s) en la lista de usuarios" % (myaccount), safetconfig.TEMPLATES[14]))


    mycheck1 = unicode(mylist[0]).rpartition("_")[0]
    mynewpass = "_"+unicode(mylist[0]).rpartition("_")[2]
    mycheck2 = "_"+mykey

#    resultstr = u"Cuenta activa: user:|%s| check1 |%s|   check2 |%s|" % (myaccount, mycheck1,mycheck2)
    resultstr = u"El código de activación de cuenta no es correcto. Verifique el enlace suministrado"
    if mycheck1 == mycheck2:
           myaction = u"operacion:Modificar_usuario Nombre_cuenta_usuario:%s Contrasena_usuario:%s" % (myaccount,mynewpass) 
           result = myinflow.toInputUsers(myaction)
	   if result:
		resultstr = u"Cuenta activada" 
	   else:
		resultstr = u"Hubo un problema al guardar la nueva contraseña"


    resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr, safetconfig.TEMPLATES[9]))
    return resultstr


def safetchangerole(req):
    sess = Session.Session(req,timeout=60*60)
    currerror =  ""
    myuser = None
    mypass = None
    form = util.FieldStorage(req,keep_blank_values=1)


    myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH) 
    resultstr = u""
    myaction = "operacion:Modificar_usuario Nombre_cuenta_usuario:erugeles Rol_usuario:Administrador" 
    result = "%d" % (myinflow.toInputUsers(myaction))
    resultstr = u"Rol fue cambiado resultado: |%s|" % (result)
 
    myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
    myinflow.setHostURL(safetconfig.SERVER_URL)     
    resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr, safetconfig.TEMPLATES[9]))
    return resultstr

def safetchangepassword(req):
    sess = Session.Session(req,timeout=60*60)
    currerror =  ""
    myuser = None
    mypass = None
    form = util.FieldStorage(req,keep_blank_values=1)
    myone = form.get("passwordone",None)
    mytwo = form.get("passwordtwo",None)


    myaccount = form.get("account",None)

    myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
    myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
    myinflow.setHostURL(safetconfig.SERVER_URL)     
 
    resultstr = u""
    if myone == mytwo: 
    	myaction = u"%s" % ("operacion:Modificar_usuario Nombre_cuenta_usuario:%s Contrasena_usuario:%s" %  (myaccount,myone)  )
	result = myinflow.toInputUsers(myaction)
	if result:
	     resultstr = u"La contraseña fue correctamente cambiada." 
	else:
	     resultstr = u"Hubo un problema al tratar de cambiar la contraseña. Consulte al administrador." 
    else:
	resultstr = u"Los valores que introdujo no son iguales. Deben ser iguales para que pueda cambiar la contraseña" 
 
    resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr, safetconfig.TEMPLATES[9]))
    return resultstr



def safetgoregister(req):
    sess = Session.Session(req,timeout=60*60)
    currerror =  ""
    form = util.FieldStorage(req,keep_blank_values=1)
    myuser = form.get("username",None)
    mypass = form.get("password",None)


    myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH) 
    if myuser != None:	
	    myinflow.registerLogin(myuser)
	    result = myinflow.login(myuser,mypass)

    resultstr = u""
    if False:
	    sess['inflow'] = True
	    sess['user'] = myuser
	    sess['pass'] = mypass	    
	    sess.save()    	
	    resultstr = printlinks()   
		 
    else:
	    resultstr = safetconfig.SAFETREGISTER
#	    myinflow.log(u"LOGFAIL:Falló la autenticación para \"%s\" con contraseña \"%s\"" % (myuser,mypass) )

    myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
    myinflow.setHostURL(safetconfig.SERVER_URL)    
#    myinflow.generateCaptcha() 
    resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr, safetconfig.TEMPLATES[14]))
    return resultstr


def safetresendpassword_16(req):
    sess = Session.Session(req,timeout=60*60)
    currerror =  ""
    form = util.FieldStorage(req,keep_blank_values=1)
    myuser = form.get("username",None)
    mypass = form.get("password",None)

    myaccount = form.get("account",None)

    myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
    myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
    myinflow.setHostURL(safetconfig.SERVER_URL)     



    if myaccount == None or len(myaccount)==0:
	 return u"%s" % (myinflow.loadReportTemplate(u"Debe colocar un nombre de cuenta", safetconfig.TEMPLATES[14]))

    mylist = myinflow.getInfoOfUser(myaccount)
    if len(mylist) == 0:
	 return u"%s" % (myinflow.loadReportTemplate(u"No se encuentra el nombre de cuenta en la lista de usuarios", safetconfig.TEMPLATES[14]))

    print "list count %d" % (len(mylist))

    print "mypass:%s" % (mylist[0])
    mynewpass = unicode(mylist[0])
    if mynewpass.startswith("_"):
 	 return u"%s" % (myinflow.loadReportTemplate(u"El nombre de cuenta ya está en proceso de reinicio.", safetconfig.TEMPLATES[14]))
    

    myrandom = sha.sha("%s" % (random.uniform(0,1000))).hexdigest()
    mylink = "%s_%s" % (myaccount,myrandom)
    mynewpass = "_%s_%s" % (mylink,mynewpass)
    myaction = "operacion:Modificar_usuario Nombre_cuenta_usuario:%s Contrasena_usuario:%s" % (myaccount,mynewpass)
 
    result =  myinflow.toInputUsers(myaction)
         

    if result:     
	    resultstr = u"Contraseña fue reiniciada."
	    result = myinflow.sendCheckEmail(myaccount,mylink)
	    if result:
		    resultstr = resultstr + u"Correo fue enviado a su cuenta. Siga el enlace para completar el cambio"
	    else: 
		    resultstr = resultstr + u"Hubo problemas para enviar el correo. Espero dos (2) horas y de no llegar el correo de activación contacte al administrador"
    resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr, safetconfig.TEMPLATES[14]))
    return resultstr

def safetresendpassword(req):
    sess = Session.Session(req,timeout=60*60)
    currerror =  ""
    form = util.FieldStorage(req,keep_blank_values=1)
    myuser = form.get("username",None)
    mypass = form.get("password",None)

    myaccount = form.get("account",None)

    myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
    myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
    myinflow.setHostURL(safetconfig.SERVER_URL)



    if myaccount == None or len(myaccount)==0:
         return u"%s" % (myinflow.loadReportTemplate(u"Debe colocar un nombre de cuenta", safetconfig.TEMPLATES[14]))

    mylist = myinflow.getInfoOfUser(myaccount)
    if len(mylist) == 0:
         return u"%s" % (myinflow.loadReportTemplate(u"No se encuentra el nombre de cuenta en la lista de usuarios", safetconfig.TEMPLATES[14]))

    print "list count %d" % (len(mylist))

    print "mypass:%s" % (mylist[0])
    mynewpass = unicode(mylist[0])
    if mynewpass.startswith("_"):
         return u"%s" % (myinflow.loadReportTemplate(u"El nombre de cuenta ya está en proceso de reinicio.", safetconfig.TEMPLATES[14]))


    myrandom = sha.sha("%s" % (random.uniform(0,1000))).hexdigest()
    mycompletelink = "%s/gochangepassword/%s_%s" % (safetconfig.SERVER_URL,myaccount,myrandom)
    mylink = "%s_%s" % (myaccount,myrandom)
    mynewpass = "_%s_%s" % (mylink,mynewpass)
    myaction = "operacion:Modificar_usuario Nombre_cuenta_usuario:%s Contrasena_usuario:%s Tickets_usuario: ABCEDFFDEFGA;1111AAAA111;111AAA111" % (myaccount,mynewpass)

    result =  myinflow.toInputUsers(myaction)


    if result:
            resultstr = u"Contraseña fue reiniciada."
            result = myinflow.sendCheckEmail(myaccount,mycompletelink)
            if result:
                    resultstr = resultstr + u"Correo fue enviado a su cuenta. Siga el enlace para completar el cambio"
            else:
                    resultstr = resultstr + u"Hubo problemas para enviar el correo. Espero dos (2) horas y de no llegar el correo de activación contacte al administrador"
    resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr, safetconfig.TEMPLATES[14]))
    return resultstr




def safetgoresendpassword(req):
    sess = Session.Session(req,timeout=60*60)
    currerror =  ""
    form = util.FieldStorage(req,keep_blank_values=1)
    myuser = form.get("username",None)
    mypass = form.get("password",None)


    myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH) 
    resultstr = u""
    resultstr = safetconfig.SAFETRESENDPASSWORD

    myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
    myinflow.setHostURL(safetconfig.SERVER_URL)     
    resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr, safetconfig.TEMPLATES[14]))
    return resultstr


def safetgologin(req):
    sess = Session.Session(req,timeout=60*60)
    currerror =  ""
    form = util.FieldStorage(req,keep_blank_values=1)
    myuser = form.get("username",None).strip()
    mypass = form.get("password",None).strip()
	
    myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH) 
    myinflow.registerLogin(myuser)
    result = myinflow.login(myuser,mypass)
    resultstr = u""
    if result:
	    sess['inflow'] = True
	    sess['user'] = myuser
	    sess['pass'] = mypass	    
	    sess.save()    	
	    resultstr = printlinks()   		 
    else:
	    resultstr = safetconfig.SAFETGOLOGIN
	    myinflow.log(u"LOGFAIL:Falló la autenticación para \"%s\" con contraseña \"%s\"" % (myuser,mypass) )

    myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
    myinflow.setHostURL(safetconfig.SERVER_URL)    
    if result: 
	    resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr, safetconfig.TEMPLATES[11]))
    else:
	    resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr, safetconfig.TEMPLATES[9]))

    return resultstr

def safetgoinputform(req):
	generalform = safetconfig.HTML_SAFETGOINPUTFORM

	sess = Session.Session(req,timeout=60*60)
	
	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
        myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
	myinflow.setHostURL(safetconfig.SERVER_URL)     
	if not sess.has_key('inflow'):	
		resultstr =  u"No es posible ejecutar esta acción, ya que no se ha autenticado"
        	resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr,safetconfig.TEMPLATES[0]))
		return resultstr 

	if not sess['inflow']:
		resultstr =  u"No es posible ejecutar esta acción, ya que la autenticación ha fallado"
        	resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr, safetconfig.TEMPLATES[0]))
		return resultstr 

    	result = myinflow.login(sess['user'],sess['pass'])
 
	resultstr = u"<nada>"
    	if result:
  		myinflow.setInputPath(safetconfig.HOMESAFET_PATH + "/.safet/input/deftrac.xml")
		myinflow.setHostURL(safetconfig.SERVER_URL)     
		resultstr = unicode(myinflow.menuCommands())
    	else:
		resultstr = u"Falló la autenticación"


	resultstr = resultstr
 
	myinflow.setHostURL(safetconfig.SERVER_URL)     
        resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr,safetconfig.TEMPLATES[5]))
 
	return resultstr

def safettests(sess):
	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
        myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
	myinflow.setHostURL(safetconfig.SERVER_URL)     
	if not sess.has_key('inflow'):
		resultstr =  u"No es posible ejecutar esta acción, ya que no se ha autenticado"
        	resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr, safetconfig.TEMPLATES[0]))
		return resultstr
	if not sess['inflow']:
        	resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr, safetconfig.TEMPLATES[0]))
		return resultstr
	return u""

def safetgoinputconsolemenu(req):
	generalform = u""
	sess = Session.Session(req,timeout=60*60)
	resultstr = safettests(sess)
	if len(resultstr) > 0:
		return resultstr
	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
	
    	result = myinflow.login(sess['user'],sess['pass'])
 
	resultstr = u"<nada>"
    	if result:
  		myinflow.setInputPath(safetconfig.HOMESAFET_PATH + "/.safet/input/defconsole.xml")
		myinflow.setHostURL(safetconfig.SERVER_URL)     
		resultstr = unicode(myinflow.menuCommands())
    	else:
		resultstr = u"Falló la autenticación"
	resultstr = resultstr 
        myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
	myinflow.setHostURL(safetconfig.SERVER_URL)     
        resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr,safetconfig.TEMPLATES[1]))
 
	return resultstr


def safetloaddata(req):
	sess = Session.Session(req,timeout=60*60)
	resultstr = safettests(sess)
	if len(resultstr) > 0:
		return resultstr


	
	form = util.FieldStorage(req,keep_blank_values=1)
	
    	myid = form.get("id",None).strip()
    	myop = u"%s"  % (form.get("op",None).decode("utf-8") ) 
    	mypri =u"%s"  % (form.get("primary",None).decode("utf-8") )
    	mymod =u"%s"  % (form.get("modname",None))
	myfs = u"%s"  % (form.get("formstring",None).decode("utf-8") )
	myother = u"%s"  % (form.get("formkey",None).decode("utf-8") ) 
	print dir(form) 
	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
    	result = myinflow.login(sess['user'],sess['pass'])
 	resultstr = u""
    	if result:
  		myinflow.setInputPath(safetconfig.HOMESAFET_PATH + "/.safet/input/%s.xml" % (mymod))
		myform = QStringList()
		for f in myfs.split("\n"):
			if len(f) > 0:
				myform.append(f)
		myupdate = unicode(myinflow.generateModifyHTML(myop,mypri,myid, myother,myform))
		#myupdate = u"inflow"
		resultstr = myupdate
    	else:
		resultstr = u"Falló la autenticación"
	return resultstr



def safetgenerateform(req,selurl):

	nameoperation = selurl
	sess = Session.Session(req,timeout=60*60)
	resultstr = safettests(sess)
	if len(resultstr) > 0:
		return resultstr

	
	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
    	result = myinflow.login(sess['user'],sess['pass'])

    	if result:
		myinflow.setHostURL(safetconfig.SERVER_URL)     
		myinflow.setHostMediaPath(safetconfig.MEDIA_URL)
		myinflow.setInputPath(safetconfig.HOMESAFET_PATH + "/.safet/input/deftrac.xml")
		resultstr = unicode(myinflow.generateFormHead(selurl))	
		resultstr = resultstr + unicode(myinflow.menuForm(selurl))
    	else:
		resultstr = u"Falló la autenticación"

	resultstr = resultstr + unicode(myinflow.generateFormFooter(selurl))
        myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)

	myinflow.setHostURL(safetconfig.SERVER_URL)     
        resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr,safetconfig.TEMPLATES[6]))
 
	return resultstr

def safetgenerateconsole(req,selurl):
	nameoperation = selurl
	sess = Session.Session(req,timeout=60*60)
	resultstr = safettests(sess)
	if len(resultstr) > 0:
		return resultstr

	
	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
    	result = myinflow.login(sess['user'],sess['pass'])
	print "safetgenerateconsole1"
    	if result:
		myinflow.setHostURL(safetconfig.SERVER_URL)     
		myinflow.setHostMediaPath(safetconfig.MEDIA_URL)
		myinflow.setInputPath(safetconfig.HOMESAFET_PATH + "/.safet/input/defconsole.xml")
		resultstr = unicode(myinflow.generateFormHead(selurl))	
		resultstr = resultstr + unicode(myinflow.menuForm(selurl))
    	else:
		resultstr = u"Falló la autenticación"


	resultstr = resultstr + unicode(myinflow.generateFormFooter(selurl))
        myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
	myinflow.setHostURL(safetconfig.SERVER_URL)     
        resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr, safetconfig.TEMPLATES[7]))
 
       # resultstr = resultstr + unicode(myinflow.generateFormFooter(selurl))
	return resultstr


def safetgoinputconsole(req):
	generalform = safetconfig.JS_SAFETGOINPUTCONSOLE

	sess = Session.Session(req,timeout=60*60)
	resultstr = safettests(sess)
	if len(resultstr) > 0:
		return resultstr

	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
        myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
	myinflow.setHostURL(safetconfig.SERVER_URL)     
        resultstr = u"%s" % (myinflow.loadReportTemplate(generalform, safetconfig.TEMPLATES[7]))
	return resultstr


def requestToForm(req,currerror):
	myform = []
	textform = req.read().decode("latin_1")
	pattern = u'name="([a-zA-Z0-9]+)"\\s+([a-zA-Z0-9áéíóúÁÉÍÓÚñÑ_¿¡\-,;\./_][a-zA-Z0-9\\s:áéíóúÁÉÍÓÚñÑ_¿¡\-,;\./_]+)-----------------------------'
	myform = re.findall(pattern,textform,re.MULTILINE)
	if len(myform) == 0:
		currerror = textform
	return myform

def safetinsert(req):
    resultstr = u""
    sess = Session.Session(req,timeout=60*60)
    resultstr = safettests(sess)
    if len(resultstr) > 0:
		return resultstr
  
    currerror = ""
    form = util.FieldStorage(req,keep_blank_values=1)
    myoperation = form.get("inputform",None).strip()

    myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
    result = myinflow.login(sess['user'],sess['pass'])
 
    if result:
  	isinserted = myinflow.toInputForm(myoperation)
	if isinserted == "Ok":
		resultstr = resultstr + u"Se ha realizado la operación <b>correctamente</>....ok"
	else:
		resultstr = resultstr + u"La operación  <b>NO</b> fue realizada.<br/>"
		myerror = myinflow.currentError().toLatin1().data()
		resultstr = resultstr +  u"El error fue el siguiente:<br/>%s" % ( myerror.decode("latin_1"))
    else:
	resultstr = u"Falló la autenticación"

    resultstr = resultstr + '<br/> <a href="/intranet/goinputform">Ir a Panel de Operaciones <b>SAFET</b></a>'
    return resultstr

def safetconsole(req,selurl):
    resultstr = u""
    sess = Session.Session(req,timeout=60*60)
    resultstr = safettests(sess)
    if len(resultstr) > 0:
		return resultstr

    currerror = ""
    form = util.FieldStorage(req,keep_blank_values=1)
    myoperation = form.get("inputform",None).decode("latin_1")
#    myoperation = "operacion:Generar_grafico_coloreado Cargar_archivo_flujo: /home/usuario/.safet/flowfiles/flujogeneral.xml"	
    myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
    myinflow.setMediaPath(safetconfig.MEDIA_PATH)
    result = myinflow.login(sess['user'],sess['pass'])
 
    if result:
  	isgood = myinflow.toInputConsole(myoperation.strip())
	currtemplate = safetconfig.TEMPLATES[7]
	if isgood:
		response  = u"%s" % (myinflow.currentJSON())
		if response.endswith(".png"):	
			resultstr = u"""
<html>
<head>
			"""

			mytitle = myinflow.currentGraphTitle();
			if mytitle.count()>0:
				resultstr = resultstr + "<title>%s</title>" % (mytitle)
			else:
				resultstr = resultstr + "<title>%s</title>" % ("Sistema Automatizado para la Firma y Estampillado de Tiempo - SAFET")
		
			resultstr = resultstr + """
</head>
<body>
			"""
			if mytitle.count() > 0:	
				resultstr = resultstr +u"<h2>%s</h2></br>" % (mytitle)
			myts = myinflow.addInfoGraphDateText()
			if myts.count() > 0:
				resultstr = resultstr +u"<b>%s</b></br>" % (myts)
			resultstr = resultstr + u"<div align=\"center\"><img src=\"%s/%s\"></img></div>" % (safetconfig.MEDIA_URL,response)

		elif response.endswith(".svg"):
			resultstr = u"""
			"""
			mytitle = myinflow.currentGraphTitle();
			if mytitle.count()>0:
				resultstr = resultstr + "<title>%s</title>" % (mytitle)
			else:
				resultstr = resultstr + "<title>%s</title>" % ("Sistema Automatizado para la Firma y Estampillado de Tiempo - SAFET")
			resultstr = resultstr + safetconfig.JS_SAFETCONSOLE
                         
                        resultstr = resultstr + " var svg = $('#svgload').svg({loadURL: '%s/%s',onLoad: null, settings: {changeSize: false} });" % (safetconfig.MEDIA_URL, response)
		        resultstr = resultstr + safetconfig.JS_SAFETCONSOLE_FUNCTIONS
    
			if mytitle.count() > 0:	
				resultstr = resultstr +u"<h2>%s</h2></br>" % (mytitle)
		        myts = myinflow.addInfoGraphDateText()
			if myts.count() > 0:
				resultstr = resultstr +u"<b>%s</b></br>" % (myts)
		        resultstr = resultstr + safetconfig.JS_SAFETCONSOLE_BOTTOM

		elif response.endswith("##SAFETMESSAGE##"):
			response = response.replace("##SAFETMESSAGE##","")
			currtemplate = safetconfig.TEMPLATES[8]
		        myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
              		response = response + u"<br/> <a href=\"%s\">Regresar a la Consulta</b></a>" % (selurl.replace("consola:","defconsole:operacion:")) 
			resultstr = u"%s" % (myinflow.loadReportTemplate(response,currtemplate))

			return resultstr
		else:			
			currtemplate = safetconfig.TEMPLATES[3]
		        myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
		        resultstr = u"%s" % (myinflow.loadReportTemplate(response,currtemplate))
			return resultstr
	else:
		resultstr = resultstr + u"La operación  <b>NO</b> se realizó.<br/>"
		myerror = myinflow.currentError().toLatin1().data()
		resultstr = resultstr +  u"El error fue el siguiente:<br/>%s" % ( myerror.decode("latin_1"))

	mylist = myinflow.lastInfoGraph()
	sess['codegraph'] = mylist[0]
	sess['dategraph'] = mylist[1]
	sess['currenttable'] = myinflow.currentTable()
	sess.save()
        resultstr = resultstr + u"<br/> <a href=\"%s\">Regresar a la Consulta</b></a>|  <a href=\"#\" id=\"savegraphbutton\" name=\"savetgraphbutton\" onClick=\"jsSaveGraph('%s')\">Guardar Grafo</a> | <a href=\"%s/%s\">Bajar archivo SVG</a>" % (selurl.replace("consola:","defconsole:operacion:"),myinflow.hostURL(),safetconfig.MEDIA_URL, response)
	resultstr = resultstr + ""
        myinflow.setTemplatePath(safetconfig.TEMPLATES_URL)
	myinflow.setHostURL(safetconfig.SERVER_URL)     
        resultstr = u"%s" % (myinflow.loadReportTemplate(resultstr,currtemplate))
 
	return resultstr 



def safetlist():
   resultstr = ""
   return resultstr

def safetgoeditor(req):
#    path = os.path.dirname(__file__)
    path = ""
    form = util.FieldStorage(req,keep_blank_values=1)		
    resultstr = u""
    sess = Session.Session(req,timeout=60*60)
    if not sess.has_key("inflow"):
        	return u"No se iniciado la sesión"
    if not sess['inflow']:
        	return u'No se ha autenticado. Siga este <a href="%s">enlace</a>  para autenticarse' % (safetconfig.LOGIN_URL)


    template_index = open("/var/www/media/templates/editor.html")
    str_tmp_idx = u"%s" % (template_index.read().decode("utf-8"))


    xml_file_name = u""
    #obtener valores enviados por POST o GET
    mystr = ""
    for k in form.keys():
		confk = k.decode("latin_1")	
		if confk.startswith("Cargar_"):	
			mystr =  form.get(confk,"").decode("latin_1").strip()
			xml_file_name = form.get(confk,"").decode("latin_1").strip()
    xml_file = open(xml_file_name)
    str_xml = u"%s" % ( xml_file.read().decode("latin_1") ) 
    #reemplaza los &lt; y &gt; por &amp;lt; y &amp;gt;
    #para que no sean interpretados por el navegador
    str_xml = u"%s" % (str_xml.replace('&lt;', '&amp;lt;'))
    str_xml = u"%s" % (str_xml.replace('&gt;', '&amp;gt;'))

    str_tmp_idx = (str_tmp_idx.replace(u'{{XML_CONTENT}}',str_xml))
    index = str_tmp_idx.replace(u'{{XML_FILE_NAME}}',xml_file_name)

#    req.content_type = "text/html"
#    req.write(index)
#    return
    return index

def safetsaveeditor(req):
#    path = os.path.dirname(__file__)
    path = ""
    #obtener valores enviados por POST o GET
    form = util.FieldStorage(req,keep_blank_values=1)		
    resultstr = u""
    sess = Session.Session(req,timeout=60*60)
    if not sess.has_key("inflow"):
        	return u"No se iniciado la sesión"
    if not sess['inflow']:
        	return u'No se ha autenticado. Siga este <a href="%s">enlace</a>  para autenticarse' % (safetconfig.LOGIN_URL)

    xml_file_name = form.get("name","").strip()
    xml_str = form.get("xml_str","").replace('\\n','\n')
    xml_str = xml_str.replace('{{gt}}','&gt;');
    xml_str = xml_str.replace('{{lt}}','&lt;');
    xml_file = open(xml_file_name,mode='w')
    xml_file.write(xml_str)
    xml_file.close()
    return 'ok'


recaptcha_private_key = '6LcoN9gSAAAAAGOqcxVsYRRPOBPDsf6sU3OLNoQ8'

recaptcha_server_name = 'http://www.google.com/recaptcha/api/verify'
recaptcha_server_form = 'https://www.google.com/recaptcha/api/challenge'

def check (client_ip_address, recaptcha_challenge_field, recaptcha_response_field):
    """Return the recaptcha reply for the client's challenge responses"""
    params = urllib.urlencode(dict(privatekey=recaptcha_private_key,
                                   remoteip=client_ip_address,
                                   challenge=recaptcha_challenge_field,
                                   response=to_bytestring(recaptcha_response_field)))
    data = None
    try:
        f = urllib2.urlopen(recaptcha_server_name, params)
        data = f.read()
        f.close()
    except HTTPError:
        pass
    except URLError:
        pass
    return data

def confirm (client_ip_address, recaptcha_challenge_field, recaptcha_response_field):
    """Return True/False based on the recaptcha server's reply"""
    result = False
    reply = check (client_ip_address, recaptcha_challenge_field, recaptcha_response_field)
    if reply:
        if reply.lower().startswith('true'):
            result = True
    return result

def xmlResponse(st,meg,fl):
        xmlcadena = u"<response> <status> </status> <message> </message> <flow> </flow> </response>"
        xmlcadenadoc = xml.dom.minidom.parseString(xmlcadena)
        for n in xmlcadenadoc.getElementsByTagName("response"):
                n.getElementsByTagName('status')[0].childNodes[0].nodeValue = st
                n.getElementsByTagName('message')[0].childNodes[0].nodeValue = meg
                n.getElementsByTagName('flow')[0].childNodes[0].nodeValue = fl
                response = n.toxml()
        return ("<?xml version=\"1.0\"?> %s" % response)


def safetgenerarflujo(req,selurl):

        sess = Session.Session(req,timeout=60*60)
        form = util.FieldStorage(req,keep_blank_values=1)
        myuser = form.get("username",None).strip()
        mypass = form.get("password",None).strip()

        myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
        myinflow.registerLogin(myuser) #Registra el ingreso de un usuario en el sistema
        result = myinflow.login(myuser,mypass) #Verifica si el usuario y contraseña son validas para el sistema True o False


        currerror =  ""
        resultstr = u""
        status = ""
        message = ""
        flow = ""
        xmlcadena = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><response><status></status><message></message><flow></flow></response>"
        xmlcadenadoc = xml.dom.minidom.parseString(xmlcadena)

        if result:   # En caso de que sea True (usuario y contraseña) entra en esta seccion
                sess['inflow'] = True
                sess['user'] = myuser
                sess['pass'] = mypass
                sess.save()
                resultstr = printlinks()

        else:

                myinflow.log(u"LOGFAIL:Falló la autenticación para \"%s\" con contraseña \"%s\"" % (myuser,mypass) )
                status = "200"
		message = "Fallo la autenticacion para el usuario"
                flow = "NULL"
                response = ""
                return xmlResponse(status,message,flow)

        myinflow.setMediaPath(safetconfig.MEDIA_PATH)
        myinflow.setHostURL(safetconfig.SERVER_URL)
        myoperation = selurl.rpartition("/")[2].replace("flujo","operacion") + " "
        nameoperation = myoperation
        myfields = u""

        confk = u""
        confvalue = u""
        conffields = {}
        parsk = u""
        parsvalue = u""
        parsfields = {}
        firstvalue = ""

        for k in form.keys():
                if k.startswith("configurekey."):
                        confk = k.decode("latin_1")
                        confvalue = form.get(confk,"").decode("latin_1").strip()
                        confk = confk[len("configurekey."):]
                        if len(confvalue) > 0:
                                conffields[confk] = confvalue
                elif k.startswith("parameters."):
                        parsk = k.decode("latin_1")
                        parsvalue = form.get(parsk,"").decode("latin_1").strip()
                        parsk = parsk[len("parameters."):]
                        if len(parsvalue) > 0:
                                parsfields[parsk] = parsvalue
                elif not k.startswith("safet") :
                        newk = k.decode("latin_1")
                        newvalue = form.get(newk,"").decode("latin_1").strip()
                        if len(newvalue) > 0:
				newitem = u" %s: %s\n" % (newk, newvalue.replace(":","##SAFETCOLON##").replace(",","##SAFETCOMMA##") ) 
                                myfields =  unicode(newitem) + myfields
                                if len(firstvalue) == 0:
                                        firstvalue = newvalue
        if not conffields.has_key("GeneralOptions/generaloptions.currentflowtitle"):
                conffields["GeneralOptions/generaloptions.currentflowtitle"] = firstvalue

	myinflow.setConffileValues(conffields)
        myinflow.setParsValues(parsfields)
        myoperation = myoperation + myfields
        os.putenv("GV_FILE_PATH","/var/www/media")
        isgood = myinflow.toInputConsole(myoperation)
        currtemplate = safetconfig.TEMPLATES[2]
        response = ""

        sess.delete()
        sess.cleanup()

        if isgood:
                response  = u"%s" % (myinflow.currentJSON())
                status = "100"
                message = "Se ejecuto correctamente"
                flow = u"http://192.168.12.134/media/%s" % response

                if response.endswith(".svg"):
                       return xmlResponse(status,message,flow)

                elif response.endswith("##SAFETMESSAGE##"):
                        response = response.replace("##SAFETMESSAGE##","")
                        return response

                else:
                        resultstr = u"%s" % (myinflow.loadReportTemplate(response,currtemplate,selurl))
                        return resultstr
        else:
                status = "300"
                message = "Debe seleccionar el flujo"
                flow = "NULL"
                return xmlResponse(status,message,flow)
