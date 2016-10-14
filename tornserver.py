#-*- coding: utf-8 -*-
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import tornado.httpserver
import tornado.ioloop
#import tornado.options
import tornado.template
import tornado.web
import tornado.auth
import tornado.escape
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
import random
import string
import time
import tornado.web
import tornado.wsgi
import wsgiref.simple_server
import re
import PIL
from PIL import Image
from collections import OrderedDict
from reportes import render_to_pdf


#from torndsession.sessionhandler import SessionBaseHandler
#from captcha.image import *

import PIL
from PyQt4.QtCore import *

import re

from tornado.options import define, options

#MYHOME = "/home/vbravo/gits/gestioninterna"
MYHOME = "/home/vbravo/gits/gestioninterna"


define("port", default=8080, help="run on the given port", type=int)

sizeLarge = (320,320)
sizeSmall = (64,64)


sizeProfile = (85,100)
 
    

def resetpass(selurl):
    currerror =  ""
    myuser = None
    mypass = None

    mykey = selurl.rpartition("/")[2]
    myaccount = mykey.partition("_")[0]

    myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
    
    mylist = myinflow.getInfoOfUser(myaccount)
    if len(mylist) == 0:
         return u"%s" % ("Hola")

    mycheck1 = unicode(mylist[0]).rpartition("_")[0]
    print "mycheck1: |%s|" % (mycheck1)
    mynewpass = "_"+unicode(mylist[0]).rpartition("_")[2]
    mycheck2 = "_"+mykey
    print "mycheck2: |%s|" % (mycheck2)

    resultstr = u"El código de activación de cuenta no es correcto. Verifique el enlace suministrado"
    if mycheck1 == mycheck2:
        resultstr = u""
        resultstr = "ok"
    else:
        resultstr = u"No coindice los datos para reiniciar la contraseña"

   
    resultstr = u"ok" 
    return resultstr




class GoRegisterHandler(tornado.web.RequestHandler):
    def get(self):            
        resultstr = safetconfig.SAFETREGISTER
        loader = tornado.template.Loader(os.path.join(MYHOME,"templates"))        

        self.write(loader.load("register.html").generate())



def resendPassword(myaccount,mylist):
    currerror =  ""
    myuser = "invitado"
    mypass = "clavecomprador"


    myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
  

    myhosturl = safetconfig.SERVER_URL + "resetpass"
 #    myinflow.setHostURL( myhosturl )
	
    haslogin = myinflow.login(myuser, mypass)
    
    print "haslogin: %d"  % (haslogin)

    mynewpass = unicode(mylist[0])
    if mynewpass.startswith("_"):
         self.write("Ya reiniciado")
	 return


    myrandom = sha.sha("%s" % (random.uniform(0,1000))).hexdigest()
    mylink = "%s_%s" % (myaccount,myrandom)
    mynewpass = "_%s_%s" % (mylink,mynewpass)
    myaction = "operacion:Modificar_usuario Nombre_cuenta_usuario:%s Contrasena_usuario:%s" % (myaccount,mynewpass)

    result =  myinflow.toInputUsers(myaction)

    print "resendpassword result: %d" % (result)

    resultstr  = u""
    if result:
            resultstr = u"Contraseña fue reiniciada."
            result = myinflow.sendCheckEmail(myaccount, myhosturl + "/" + mylink)
            if result:
                    resultstr = resultstr + u"Correo fue enviado a su cuenta. Siga el enlace para completar el cambio"
            else:
                    resultstr = resultstr + u"Hubo problemas para enviar el correo."

    return resultstr 


class  DoResetPassHandler(tornado.web.RequestHandler):
    def get(self,name_operation):
	print "getDoReset"
        print "DoResetPass selurl: |%s|" % (name_operation)
        loader = tornado.template.Loader(os.path.join(MYHOME,"templates")) 
        current_user="invitado"
        current_pass="clavecomprador"
	print "DoReset ...1"
    	mykey = name_operation.rpartition("/")[2]
    	myaccount = mykey.partition("_")[0]

	result = resetpass(name_operation)
	print "DoResetPass result:%s" % (result)
	if result == "ok":
		self.write(loader.load("twopass.html").generate( myaccount = myaccount ))
		return

	self.write(loader.load("login.html").generate( mymessage = True ))

    def post(self,selurl):
	print "postDoResetPass...1"
	myone = self.get_argument("passwordone")
	mytwo =  self.get_argument("passwordtwo")

	print "postDoResetPass myone" + myone
	print "postDoResetPass mytwo" + mytwo

        loader = tornado.template.Loader(os.path.join(MYHOME,"templates")) 
        myaccount = self.get_argument("account")

	print "postDoResetPass myaccount: |%s|" % (myaccount)

        current_user="invitado"
        current_pass="clavecomprador"
	
	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
	myinflow.login(current_user,current_pass)
        
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

    	return self.write(resultstr)

	
 

class MgnResetPassHandler(tornado.web.RequestHandler):
    def get(self,name_operation):
        print "GoResetPass **get: |%s|" % (name_operation)
        loader = tornado.template.Loader(os.path.join(MYHOME,"templates")) 
        current_user="invitado"
        current_pass="clavecomprador"
        imgcaptcha = ImageCaptcha() 
        pathcaptcha = ""
        urlcaptcha = ""
        stringcaptcha = id_generator(5)
	print "pass secure 1"
        self.set_secure_cookie("stringcaptcha",stringcaptcha)
         
        print "pass 1"
        if name_operation == "gocheckuser":
	    print "pass 2"
	    idg = id_generator(1)
	    print "*****pass_3 %s" % (idg)
	
            try:
		idg = "1"
            	pathcaptcha = "/home/vbravo/gits/gestioninterna"  + "/static/captcha/out%s.png" % (idg)
	        urlcaptcha = "/static/captcha/out%s.png" % (idg)

	    	print "pass 4"
	    	print "pass stringcaptcha: %s" % (stringcaptcha)
	    	print "*pass pathcaptcha: %s" % (pathcaptcha)

                #imgcaptcha.write(stringcaptcha, pathcaptcha)
		print "pass 6"
            except Exception as e:
                print "error captcha: " + e
                return
            pathcaptcha = "/" + pathcaptcha
	    print "*pass 3"
	    try: 
		    print "pass 7"
	            self.write(loader.load("resetpass.html").generate(pathcaptcha = urlcaptcha, mymessage = None))
            except Exception as e:
		print "error reset"
                print "error reset: " + e
                return 
            return
        print "pass 2"  
        self.write(loader.load("resetpass.html").generate(mymessage = None ))
        
    def post(self,name_operation): 
         print "post: %s" % (name_operation)
         current_user="invitado"
         current_pass="clavecomprador"
         imgcaptcha = ImageCaptcha() 
         

         loader = tornado.template.Loader(os.path.join(MYHOME,"templates"))
         mycaptcha = self.get_argument("currcaptcha").strip().lower()

         datacaptcha = self.get_secure_cookie("stringcaptcha")
         if datacaptcha == None:
             print "nc"
             self.write(loader.load("login.html").generate(mymessage = True ))
             return
             
             
         datacaptcha = datacaptcha.lower()   
         print "post captcha...1:" + datacaptcha
         print "post captcha...2:" + mycaptcha
         
         
         myaccount = self.get_argument("account").strip().lower()
         print "post myaccount:" + myaccount
         myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH) 
         result = myinflow.login(current_user,current_pass)
           
         mylist = myinflow.getInfoOfUser(myaccount)
         print "post mylist count:%d" % (len(mylist))
         
#         hascaptcha = (mycaptcha == datacaptcha)
	 hascaptcha = True
         print "hascaptcha: %d" % (hascaptcha)
         
         if len(mylist) == 0 or not hascaptcha:             
             pathcaptcha = ""
             stringcaptcha = id_generator(5)
	     print "...2..."
	     idg = id_generator(1)
             pathcaptcha = safetconfig.PROJECT_PATH + "/static/captcha/out%s.png" % (idg)
             urlcaptcha =  "/static/captcha/out%s.png" % (idg)
	     print "pathcaptcha" + pathcaptcha
             try:
                imgcaptcha.write(stringcaptcha, pathcaptcha)
             except Exception as e:
                print "error captcha: " + str(e)
                return
             pathcaptcha = "/" + pathcaptcha
             self.set_secure_cookie('stringcaptcha',stringcaptcha)
             print "post pathcaptcha: |%s|" % (pathcaptcha)
             print "post stringcaptcha: |%s|" % (stringcaptcha)
             
             
             mymessage = "El usuario seleccionado o el código no coinciden, vuelva a intentar"
             self.write(loader.load("resetpass.html").generate(pathcaptcha = urlcaptcha, mymessage = mymessage))
             return
             
        
         resultstr = resendPassword(myaccount, mylist)      
	 self.write(resultstr)
        # self.write(loader.load("twopass.html").generate())
         


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

	    
class ProcessAjaxConsoleHandler(tornado.web.RequestHandler):
    def post(self):            

	print "ProcessAjaxConsoleHandler ....(1)..."
                
        current_user = self.get_secure_cookie("user")
        current_pass = self.get_secure_cookie("pass")
        
        loader = tornado.template.Loader(os.path.join(MYHOME,"templates"))        
        if not current_user:
            self.write('{ "error": "No está autenticado. No puede ingresar a esta página", "result": "false" }' )		
            return        

        myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH) 
       
        result = myinflow.login(current_user,current_pass)
        
        myoperation = myid = self.get_argument("operation").strip()
        #print "...ProcessAjaxConsoleHandler....myoperation:|%s|" % (myoperation)
        
				
        isinserted = myinflow.toInputConsole(myoperation)
        if not isinserted:   
	    myerror = u"error:%s" % (myinflow.currentError()) 
	    #print myerror
            self.write('{ "error": "No fue posible listar los datos solicitados", "result": "false" }' )		
            return            
        myjson = u"%s" % (myinflow.currentJSON())
                #mylist = json.loads(myjson)["safetlist"];
        #print u"json:%s" % (mylist)
        self.write(myjson)
        


class ProcessAjaxPanelHandler(tornado.web.RequestHandler):
  
    def get(self,name_operation,name_filter ,name_title, cp = None  ):            

	print "ProcessAjaxPanelHandler ...........(1)..."
                
        current_user = self.get_secure_cookie("user")
        current_pass = self.get_secure_cookie("pass")
        print "ProcessAjaxPanelHandler ...........(2)..."
        
        loader = tornado.template.Loader(os.path.join(MYHOME,"templates"))        
        if not current_user:
            self.write('{ "error": "No está autenticado. No puede ingresar a esta página", "result": "false" }' )		
            return        
            
        print "ProcessAjaxPanelHandler ...........(*3)..."    

        myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH) 
       
	print "ProcessAjaxPanelHandler ...........(*4)..."    
        result = myinflow.login(current_user,current_pass)
        print "ProcessAjaxPanelHandler ...........(*5)..."    
	if not result:
            self.write('{ "error": "falla en la autenticación. No puede ingresar a esta página", "result": "false" }' )		
            return        
            
        print "ProcessAjaxPanelHandler ........ajaxpanel...(*6)..."        

        
        mypage = ""
        myprefix = ""
        currpage = "0"
        print "ProcessAjaxPanelHandler ........ajaxpanel...(*7)..."        
        if cp == "none":
	      print "ProcessAjaxPanelHandler ........ajaxpanel...(*8)..."        
	      myprefix = "p_"
        elif cp != None:
	  currpage = cp
	  mypage = "parameters.CurrPage:%s"  %  currpage
	else:
	  mypage = "parameters.CurrPage:%s"  %  currpage
	 
	typeflow = "flujo"  
	
	if name_operation == "Sales":
	  typeflow = "ventas" 
	elif name_operation == "Draft":
	  typeflow = "flujo"	  
	elif name_operation == "PublishedUser":
	  typeflow = "usuario"
	  currname_operation = "Published"
        elif name_operation <> "Published":
	  typeflow = "usuario"
 
	 
        
        print "ProcessAjaxPanelHandler ...........(*4)...currpage:" + currpage
        
	myoperation = u"operacion:Listar_datos Cargar_archivo_flujo: " + safetconfig.HOMESAFET_PATH + "/.safet/flowfiles/%s%s_publicaciones.xml Variable:vPublished %s" % (myprefix,typeflow,mypage)
        
				
	print "ProcessAjaxPanelHandler ...........(5)..."    				
        isinserted = myinflow.toInputConsole(myoperation)
        if not isinserted:   
	    myerror = u"error:%s" % (myinflow.currentError()) 
	    #print myerror
            self.write('{ "error": "No fue posible listar los datos solicitados", "result": "false" }' )		
            return            
        myjson = u"%s" % (myinflow.currentJSON())
                #mylist = json.loads(myjson)["safetlist"];
        #print u"json:%s" % (mylist)
        print "ProcessAjaxPanelHandler ...........(6)..."    
        self.write(myjson)
        

class ProcessAjaxPageHandler(tornado.web.RequestHandler):
    def get(self, cp = None):            

	print "ProcessAjaxPageHandler ....(1)..."
                
        current_user = self.get_secure_cookie("user")
        current_pass = self.get_secure_cookie("pass")
        
        loader = tornado.template.Loader(os.path.join(MYHOME,"templates"))        
        if not current_user:
            self.write('{ "error": "No está autenticado. No puede ingresar a esta página", "result": "false" }' )		
            return        

        myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH) 
       
        result = myinflow.login(current_user,current_pass)
	if not result:
            self.write('{ "error": "falla en la autenticación. No puede ingresar a esta página", "result": "false" }' )		
            return        

	currpage = 0

	if cp != None:
		currpage = cp
        
	myoperation = u"operacion:Listar_datos Cargar_archivo_flujo: " + safetconfig.HOMESAFET_PATH + "/.safet/flowfiles/p_flujo_publicaciones.xml Variable:vPublished"
        
				
        isinserted = myinflow.toInputConsole(myoperation)
        if not isinserted:   
	    myerror = u"error:%s" % (myinflow.currentError()) 
	    #print myerror
            self.write('{ "error": "No fue posible listar los datos solicitados", "result": "false" }' )		
            return            
        myjson = u"%s" % (myinflow.currentJSON())
                #mylist = json.loads(myjson)["safetlist"];
        #print u"json:%s" % (mylist)
        self.write(myjson)
 

	    
    

class ProcessFilesHandler(tornado.web.RequestHandler):    
	def post(self,name_operation):
	 #    print ".........ProcessAjaxFormHandler........post:" + name_operation
	    print "ProcessFilesHandler................1"
	    current_user = self.get_secure_cookie("user")
	    current_pass = self.get_secure_cookie("pass")
        
	    loader = tornado.template.Loader(os.path.join(MYHOME,"templates"))        
	    if not current_user:
		self.write('{ "error": "No está autenticado. No puede ingresar a esta página", "result": "false" }' )		
            return        
	    
	    print "ProcessFilesHandler................2"
	    myoperation = QString(u"operacion:%1 ").arg(name_operation)
	    
	    #print "file: %d" %( len(self.request.files) )
	    currfile = ""
	    filefield = ""
	    urlfile = safetconfig.MEDIA_PATH
	    urlfile = urlfile.replace(":","__SAFETCOLON__")
	    for myfile in  self.request.files.keys():
		      #print "key: %s " % (myfile)
		      urlfile = safetconfig.MEDIA_PATH
		      urlfile = urlfile.replace(":","__SAFETCOLON__")
	   
		      for f in  self.request.files[myfile]:
			    #print u"  filename: %s " % (f["filename"])
			    #print u"  content_type: %s " % (f["content_type"])
			    currfile = u"%s/static/media/%s" % (MYHOME, f["filename"])
			    #myurlfile = urlfile + "/" + f["filename"]
			    myurlfile =  f["filename"]
			    #print currfile
			    #filefield = myfile + ":"	 
			    filefield = filefield + myfile + ":" + myurlfile + " "
			    thefile = open(currfile,"wb")
			    thefile.write(f["body"])
			    thefile.close()
	    #print "**---------------self.request.arguments:|%d|" % (len(self.request.arguments))
	    alumno_id = "0"
	    for item in self.request.arguments:
	          #print "item: %s" % (item)
		  myvalue = tornado.escape.to_unicode(self.get_argument(item))
		  #print "item: %s" % (myvalue)
		  myfield =QString(u" %1:%2").arg(item).arg(myvalue.replace(",","##SAFETCOMMA##"))
		  if item == "alumno_id":
		      alumno_id = myvalue
		      
		  if not item.startswith("safet"):
			  if len(myvalue) > 0:
			    myoperation = myoperation + myfield
	    filefield.strip()
	    myoperation = myoperation + " " + filefield
	    myoperation = myoperation.trimmed()
	    print "ProcessFilesHandler....myoperation:\n|%s|" % (myoperation)
	    
		
	    print "ProcessFilesHandler................3"
#	    print u"**********......operation(->):\n |%s|\n\n" % (myoperation)
	    myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
	    result = myinflow.login(current_user,current_pass)		
	
	    
	    isinserted = myinflow.toInputForm(myoperation  )
	    print "ProcessFilesHandler................3..." + isinserted
#	    
	    if isinserted != "Ok":
		      self.write("{ \"result\": \"false\", \"id\":\"0\", \"error\": \""+myinflow.currentError() + "\" }")
		      
		      return
	    
	    #print "myjson: %s" % (myjson)
	    myjson = u"%s" % (myinflow.currentJSON())
	    currjson = "{}"
	    try:
	      currjson = json.loads(myjson)
	    except Exception as e:
		print "exception json"
		print e
		
	    currjson["alumno_id"] = alumno_id	    
	    print "currjson...1"
	    mytext = json.dumps(currjson)
	    self.write("%s" % (mytext) )

        
        
        
   
        
class ProcessFormHandler(tornado.web.RequestHandler):    
	def post(self,name_operation,name_template,currid):
	    print "***post:" + name_operation
	    
	    current_user = self.get_secure_cookie("user")
	    current_pass = self.get_secure_cookie("pass")
        
	    current_ticket  = ""
	       	      
	    print "***ProcessForm...1"
	    print "***current_user" + current_user
	    loader = tornado.template.Loader(os.path.join(MYHOME,"templates"))        
	    if not current_user:
		self.write(loader.load("message.html").generate(mymessage=u"No está autenticado. No puede ingresar a esta página."))
		return

	      
	    myoperation = QString(u"operacion:%1 ").arg(name_operation)
	    
	    #print "file: %d" %( len(self.request.files) )
	    currfile = ""
	    hasprofile = name_operation == "modificar_perfil"    

	    urlfile = safetconfig.MEDIA_PATH
	    urlfile = urlfile.replace(":","__SAFETCOLON__")
	    filefields = ""	 
            print "Processs form 1"
	    for myfile in  self.request.files.keys():	      
		      print "*keyfile: %s " % (myfile)
		      for f in  self.request.files[myfile]:
			    print u"  filename: %s " % (f["filename"])
			    print u"  content_type: %s " % (f["content_type"])
			    currfile = u"%s/static/media/%s" % (MYHOME, f["filename"])
			    newurlfile = urlfile + "/" + f["filename"]
			    #print currfile
			    print "file1"	
			    filefield = " %s:" % (myfile)
			    filefield = filefield + newurlfile + " "
			    filefields = filefields + filefield
			    thefile = None
			    
			    try:
			    	  thefile = open(currfile,"wb")
	 		          thefile.write(f["body"])
 			          thefile.close()
		                  print "file2" 		  
				  
                                  img = Image.open(currfile) 
                                  if hasprofile:                     
                                    img = img.resize(sizeProfile, Image.ANTIALIAS)  
                                  else:  
                                    img = img.resize(sizeLarge, Image.ANTIALIAS)
                                  
                                  mypath = os.path.splitext(currfile)
                                 
                                  mynewpath = mypath[0]+ "" + mypath[1]
                                  img.save(mynewpath)
                                  mynewpath = mypath[0]+"_tb" + mypath[1]
                                  img.thumbnail(sizeSmall, Image.ANTIALIAS)
                                  img.save(mynewpath)
                            except IOError:
				print "Error 1"
                                #print "ProcessForm**Error Image:" + currfile                         
                                continue
                            except ValueError:
				print "Error 2"
                                #print "ProcessForm**Error Image:" + currfile
                                #print "ProcessForm**Error Value:" + ValueError
                                continue
			    except Exception as e:
				print e
	    filefields.strip()		    

            print "Processs form 2"
	    for item in self.request.arguments:
	      
	          #print "item: %s" % (item)
	          #print "itemtype %s" % (type(self.get_argument(item)))
		  myvalue = self.get_argument(item)
		  myvalue = escapeSafet(myvalue)
#		  myvalue = tornado.escape.to_unicode(self.get_argument(item))
		  myvalue = tornado.escape.to_unicode(myvalue)
		

		  myfield =QString(u" %1:%2").arg(item.replace(" ","_")).arg(myvalue)
		  #print u"%s" % (myfield)
		  #print ""
		  if not item.startswith("safet"):
			  if len(myvalue) > 0:
			    myoperation = myoperation + myfield
	   
	   
	    myoperation = myoperation + filefields
	    myoperation = myoperation.trimmed()
	    print u"%s" % (myoperation)
	    current_html = getForm(current_user,current_pass,name_operation,"none")	    	    	    
	    
	    if not current_html:
	        #print "not exists html"
		current_html = None
 
	    if name_operation == "agregar_respuesta":
		myoperation = myoperation + " Publicacion_id:" + currid
		
		
            print "Processs form 3"
	    myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
	    result = myinflow.login(current_user,current_pass)		
	    print "Process form result...login...|%s|" % (result)
	    
	    print "Process form result...operation:|%s| " % (myoperation)
	    
	    isinserted = myinflow.toInputForm(myoperation )	    	    
	    print "Process .........isinserted:" + isinserted
	    
	    myinflow.log("*ProcessForm")
	    myinflow.log("**myoperation:" + myoperation)
	    myuserid = 1
	        

	    menues = menuToList("/goform/addgeneric",current_user,current_pass)
	  
	  
	    print "-" * 80

	    if not isinserted:
	      
		myerror = u"%s" % (myinflow.currentError())
		print u"error:%s" % (myerror)
		self.write(loader.load("editprofile.html").generate(mycode=current_html,successmessage=None,mymessage= myerror, pubs = None, current_user = current_user,user_id = myuserid ,menues =  menues ))
		return

	    currpostaction = myinflow.postAction()
	    
	    
	    myresult = executeFormAction(current_user, current_pass, currpostaction)
	    

	    print "-" * 80
	    #mydir = u"/goform/%s/%s/%s" % (name_template,name_operation, currid)
	    mydir = u"/goform/%s/%s/%s/success" % (name_template,name_operation, currid)
	    #print "mydir (redirect):%s" % (mydir)
	    if name_operation == "agregar_respuesta":
	      mydir = u"/showcomm/none/none/%s" % (currid)
	      
	    
	    self.redirect(mydir)

def executeFormAction(current_user, current_pass, action):
	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
	myinflow.setHostURL(safetconfig.SERVER_URL)     
	myinflow.setHostMediaPath(safetconfig.MEDIA_URL)
	myinflow.setInputPath(safetconfig.HOMESAFET_PATH + "/.safet/input/deftrac.xml")
	
	result = myinflow.login(current_user,current_pass)		

	if len(action) > 0:
		allpost = "%s".strip() %  (action)
		postlist = allpost.split("##SAFETSEPARATOR##")
		for currpost in postlist:
			print "before send_email"
			print "currpost: |" + currpost + "|"
			print ""
			presult = myinflow.toInputForm(currpost,False)
			print ""
			print "after send_email:"
			print "presult: " + presult
			#myinflow.log("PRESULT POSTACTION RESULT:" + presult
			
	return True		
     


def getPubs(current_user,current_pass,name_operation, par1 = "", currvar = ""):

        myjson = getPubsJson(current_user,current_pass,name_operation, par1, currvar)                        
	try:
	        mypubs = json.loads(myjson)["safetlist"]      
	except Exception as e:
		print "has getPubs exception error"
		print e
		print "....................."
		return []
		
	print "return mypubs" 
        return mypubs


def getForm(current_user,current_pass,name_operation,currid, name_template = "gopublish"):
	    myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
	    myinflow.setHostURL(safetconfig.SERVER_URL)     
	    myinflow.setHostMediaPath(safetconfig.MEDIA_URL)
	    myinflow.setInputPath(safetconfig.HOMESAFET_PATH + "/.safet/input/deftrac.xml")

	    result = myinflow.login(current_user,current_pass)    
	    #print  "(global) result:%d"  % (result)
	    
	    selurl = u"/deftrac:operacion:%s" % (name_operation)	    
      
	    html1 = "" 
	    if currid == "none":
		html1 = unicode(myinflow.generateFormHead(selurl))  
	    else:	
	        myvalue =  u'<SAFETSEPARATOR/>[value="%s"]' % (currid)
		html1 = unicode(myinflow.generateFormHead(selurl+ myvalue))  
	    
	    
	    html2 = unicode(myinflow.menuForm(selurl))           
	    html2 = html2.replace("{{SAFETCURRID}}",u"/%s/%s" % (name_template,currid))

	    html3 = unicode(myinflow.generateFormFooter(selurl))
	    
	    current_html = html1 + html2 + html3
	    	
	    return current_html                

def getUserInfo(current_user,current_pass, operation):
	     myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH) 

             result = myinflow.login(current_user,current_pass)
        
	     #myoperation = u"operacion:Listar_datos Cargar_archivo_flujo: " + safetconfig.HOMESAFET_PATH + "/.safet/flowfiles/usuarioscuenta.xml Variable: vTodas parameters.ByAccount:" + current_user   
	     myoperation = operation
	     #print myoperation
	     isinserted = myinflow.toInputConsole(myoperation)
	     #print isinserted
	     if not isinserted:   
		myerror = u"%s" % (myinflow.currentError()) 
		#print myerror
		return myerror
	      
	     myjson = u"%s"  % (myinflow.currentJSON())
	     #print myjson
	     result = json.dumps(json.loads(myjson)["safetlist"])
	     
	     return result                
        

class LoginHandler(tornado.web.RequestHandler):

    def post(self):           
	print "LoginHandler...pass...1" 
        self.myuser = self.get_argument("account")
        mypass = self.get_argument("passwordone")
        myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH) 

        loader = tornado.template.Loader(os.path.join(MYHOME,"templates"))                
        myinflow.registerLogin(myuser)
        result = myinflow.login(myuser,mypass)        
        if result:
            print "panel entering..."            
            goPanel()            
        else:
            self.write(loader.load("message.html").generate(mymessage= "<font color=red>El nombre de la cuenta o clave no es correcta"))

    def goPanel(self):
	 print "LoginHandler................redirigiendo........"
#	 self.redirect("goform/addgeneric/agregar_Alumno/0")	
	 self.redirect("goform/addgeneric/Modificar_solicitud_vacaciones/0")	
	 return
#        mypubs = []
 #       mypubs.append({ "summary": "Venta 2"})
#        self.write(loader.load("panel.html").generate(pubs = mypubs, name_operation = "All", current_user = self.myuser ) )



class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        #print "Logout"
        self.clear_cookie("user")
        self.clear_cookie("pass")
        self.clear_cookie("ticket")
        loader = tornado.template.Loader(os.path.join(MYHOME,"templates"))        
        self.write(loader.load("login.html").generate(mymessage=False))

   
def isInList(thekey, thesecondkey, thelist):
      for l in thelist:
	  if l[thesecondkey] == thekey:
	      return True
      return False
	
def escapeSafet(currstr):
    result = currstr
    result = currstr.replace("<","&lt;")
    result = result.replace(">","&gt;")
    result = result.replace(":","__SAFETCOLON__")
#    result = result.replace("\"","&#39;")
    result = result.replace("\"","&quot;")
    result = u"%s" % (result.replace(u"&aacute;",u"á"))
    result = u"%s" % (result.replace(u"&eacute;",u"é"))
    result = u"%s" % (result.replace(u"&iacute;",u"í"))
    result = u"%s" % (result.replace(u"&oacute;",u"ó"))
    result = u"%s" % (result.replace(u"&uacute;",u"ú"))
    result = u"%s" % (result.replace(u"&ntilde;",u"ñ"))
    result = u"%s" % (result.replace(u"&Ntilde;",u"Ñ"))
    
    return result
	
	
        

class CheckAccountHandler(tornado.web.RequestHandler):
    def post(self):                      
	myaccount = self.get_argument("account")
        #print "Account is:|%s|" % (myaccount)
        #print "CheckAccount*"  
        
        myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH) 

	current_user = "invitado"
	current_pass = "clavecomprador"
        result = myinflow.login(current_user,current_pass)
       
        if not result:
	    self.write("error 201")
	    return
	    
        mylist = myinflow.getInfoOfUser(myaccount)
	if len(mylist) == 0:
		self.write("true")
	else:  
		self.write("false")
		
		
#        self.flush()
        

class LegacyLoadDataHandler(tornado.web.RequestHandler):
    def post(self):
        print ".....LegacyLoadDataHandler.........1"
        current_user = self.get_secure_cookie("user")
        current_pass = self.get_secure_cookie("pass")
        

        print ".....LegacyLoadDataHandler.........2"
        loader = tornado.template.Loader(os.path.join(MYHOME,"templates"))        

 	if current_user==None or len(current_user) == 0:
	    print "*************"
	    print "Current user is EMPTY"
	    current_user="invitado"
	    current_pass="clavecomprador"	    
	    self.set_secure_cookie("user", current_user)
	    self.set_secure_cookie("pass", current_pass)
	

	print ".....LegacyLoadDataHandler.........3"
        myid = self.get_argument("id").strip()

        myop = u"%s"  % (self.get_argument("op") ) 
        #mypri =u"%s"  % (self.get_argument("primary").decode("utf-8") )
        mypri =u"%s"  % (self.get_argument("primary"))        
        mymod =u"%s"  % (self.get_argument("modname"))

        myfs = u"%s"  % (self.get_argument("formstring") )
        
        print ".....LegacyLoadDataHandler.........4...myid:|%s|"  % (myid)
        print ".....LegacyLoadDataHandler.........4...op:|%s|"  % (myop)
        print ".....LegacyLoadDataHandler.........4...mypri:|%s|"  % (mypri)
        print ".....LegacyLoadDataHandler.........4...mymod:|%s|"  % (mymod)
        
       
       #myother = u"%s"  % (self.get_argument("formkey").decode("utf-8") ) 

        myother = u""
        
        
        myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
        result = myinflow.login(current_user,current_pass)
        mypath = safetconfig.HOMESAFET_PATH + "/.safet/input/%s.xml" % (mymod)
        print "mypath:" + mypath
        myinflow.setInputPath(mypath)
        myform = QStringList()
        print ".....LegacyLoadDataHandler.........5"
        for f in myfs.split("\n"):
             if len(f) > 0:
                 myform.append(f)
        print ".....LegacyLoadDataHandler.........7"         
        
        myupdate = unicode(myinflow.generateModifyHTML(myop,mypri,myid, myother,myform))
        
        print ".....LegacyLoadDataHandler.........6"    
       # print "*********myupdate....:|%s|"  % (myupdate)
        
        print "*********myupdate: len:%d"  % (len(myupdate))
        self.write(myupdate)
        

class ListHandler(tornado.web.RequestHandler):
    def get(self,nameflow,namevar):
        print ".....ListHandler.........1"
        current_user = self.get_secure_cookie("user")
        current_pass = self.get_secure_cookie("pass")
        
        loader = tornado.template.Loader(os.path.join(MYHOME,"templates"))        
        if not current_user:
            self.write('{ "error": "No está autenticado. No puede ingresar a esta página", "result": "false" }' )		
            return        


        print ".....ListHandler.........2"
        loader = tornado.template.Loader(os.path.join(MYHOME,"templates"))        

    
        myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
        result = myinflow.login(current_user,current_pass)
     
	print ".....ListHandler.........3"
     	myoperation = u"operacion:Listar_datos Cargar_archivo_flujo: " + safetconfig.HOMESAFET_PATH + "/.safet/flowfiles/%s.xml Variable: %s" % (nameflow,namevar)
    
	print "*** myoperation**"
	print myoperation
	print "*" * 80
	print ".....ListHandler.........4"
	isinserted = myinflow.toInputConsole(myoperation)
	print isinserted
	
	print ".....ListHandler.........5"
	mylist = []
	if isinserted:
		  mystr = u"%s" % (myinflow.currentJSON())
		  #print "*" * 80
		  #print u"JSON....mystr:|%s|" % (mystr)
		  #print "*" * 80
		  mylist = json.loads(mystr, object_pairs_hook=OrderedDict)["safetlist"]
		  
		  
			  
	else:
		  mystr = u"%s" % (myinflow.currentError())		  
		  print "error: %s" % (mystr)
	
#	print "....ListHandler...write"	
#	print "*" * 80
#	print mylist[0]
#	print "*" * 80
	mykeys = []
#	print "1." + ("*" * 80)
	mycount = len(mylist)
	menues = menuToList("/goform/addgeneric",current_user,current_pass)
	if mycount > 0:
		mykeys = mylist[0].keys()
	
	
    	self.write(loader.load("listparents.html").generate(mylist = mylist, mykeys = mykeys, current_user = current_user, user_id=1, mycount = mycount, menues = menues))

	

# Clase para mostrar la interfaz de carga de gestion interna
class LoadScoreHandler(tornado.web.RequestHandler):
    def get(self):
        print ".....LoadScoreHandler.........1"
        
        loader = tornado.template.Loader(os.path.join(MYHOME,"templates"))        

	print ".....LoadScoreHandler.........2"

        self.write(loader.load("loadscore.html").generate(current_user ="vbravo", user_id=1))


# ruta abdoluta del directorio que mantiene la gestión interna al ser cargadas
absoluteDirectoryPath = "/tmp"

# funcion para crear un directorio temporal con los archivos de boletas
def createDirectory(gradeSection, lapse):
	print "createDirectory()..." 
	#print gradeSection
	#print lapse
	
	# crear directorio /tmp/gradeSection-lapse
	directory = absoluteDirectoryPath+"/"+gradeSection+"-"+lapse
	if not os.path.exists(directory):
    		os.makedirs(directory)
	removeDir(directory)
	os.makedirs(directory)
	print "directory "+absoluteDirectoryPath+"/"+gradeSection+"-"+lapse+" created"
	return absoluteDirectoryPath+"/"+gradeSection+"-"+lapse

# funcion para borrar un directorio existente
def removeDir(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
	
	
	
       
        
class LoadDataHandler(tornado.web.RequestHandler):
    def post(self):                	
	myid = self.get_argument("id")

   #	current_user = self.get_secure_cookie("user")
   #     current_pass = self.get_secure_cookie("pass")
       
        current_user = self.get_secure_cookie("user")
        current_pass = self.get_secure_cookie("pass")
        
        loader = tornado.template.Loader(os.path.join(MYHOME,"templates"))        
        if not current_user:
            self.write('{ "error": "No está autenticado. No puede ingresar a esta página", "result": "false" }' )		
            return        
     
 
   	

	#print "myid: %s" % (myid)
	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH) 
	myinflow.login(current_user,current_pass)
        print "....LoadData...1....myid:%s" % (myid)


	    #print "Country is:|%s|" % (self.get_argument("country"))
	print "myid 2"
	    
	myoperation = u"operacion:Listar_datos Cargar_archivo_flujo: " + safetconfig.HOMESAFET_PATH + "/.safet/flowfiles/representantes.xml Variable: vTodas parameters.ById:%s" % (myid)
    
	print myoperation
	isinserted = myinflow.toInputConsole(myoperation)

	#print isinserted
	if isinserted:
		  mystr = u"%s" % (myinflow.currentJSON())
		  print "JSON"
		  print mystr
		  self.write(mystr)
	else:
		  mystr = u"%s" % (myinflow.currentError())		  
		  print "error> %s" % (mystr)
		  self.write(mystr)
	    
#	    self.flush()
   

class CheckCIHandler(tornado.web.RequestHandler):
    def post(self):    
	print "checkci" 
            	
	myci = self.get_argument("ci")

	print "myId: %s" % (myci)
	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)         
    
	current_user = "invitado"
	current_pass = "clavecomprador"
        result = myinflow.login(current_user,current_pass)
       
        if not result:
	    self.write("error 201")
	
        
        myoperation = u"operacion:Listar_datos Cargar_archivo_flujo: " + safetconfig.HOMESAFET_PATH + "/.safet/flowfiles/usuarios.xml Variable: vTodas parameters.ByCI:%s" % (myci)
   
	print myoperation
	isinserted = myinflow.toInputConsole(myoperation)
	print "IsInserted: %d" % (isinserted)

	if isinserted:
	      mystr = u"%s" % (myinflow.currentJSON())	      	      
	      count  = json.loads(mystr)["safetlistcount"]
	      print mystr
	      #print "count:|%s|" % (count)
	      if count == "0":
		self.write("true")
	      else:
		self.write("false")
	else:			  
	      self.write("false")
	    
#	self.flush()
	   

class CheckRIFHandler(tornado.web.RequestHandler):
    def post(self):    
	print "checkci" 
            	
	myrif = self.get_argument("rif")

	print "myId: %s" % (myrif)
	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)         
    
	current_user = "invitado"
	current_pass = "clavecomprador"
        result = myinflow.login(current_user,current_pass)
       
        if not result:
	    self.write("error 201")
	
        
        myoperation = u"operacion:Listar_datos Cargar_archivo_flujo: " + safetconfig.HOMESAFET_PATH + "/.safet/flowfiles/rifes.xml Variable: vTodas parameters.ByRIF:%s" % (myrif)
   
	print myoperation
	isinserted = myinflow.toInputConsole(myoperation)
	print "IsInserted: %d" % (isinserted)

	if isinserted:
	      mystr = u"%s" % (myinflow.currentJSON())	      	      
	      count  = json.loads(mystr)["safetlistcount"]
	      print mystr
	      #print "count:|%s|" % (count)
	      if count == "0":
		self.write("true")
	      else:
		self.write("false")
	else:			  
	      self.write("false")
	    


    
class RegisterHandler(tornado.web.RequestHandler):
    def post(self):           
	print "RegisterHandler" 
        currerror =  ""

        myaccount =  self.get_argument("account")
        print "**myaccount:%s" %(myaccount)

        myfirstname = self.get_argument("firstname")
        mylastname = self.get_argument("lastname")
        myci = self.get_argument("ci")
	myrif = ""
	mycinac = ""
	myrifnac = ""



	
	try:
		myrif = self.get_argument("rif")
		if len(myrif)>0:
		    myrif = " rif:%s" % (myrif)
	except Exception as e:
		print "no rif" 
		print e

	try:
	    mycinac = " cedula_nac: %s " % (self.get_argument("ci_nac"))
	    myrifnac = " rif_empresa_nac: %s " % (self.get_argument("rif_empresa_nac"))

	except Exception as e:
		print "no ci_nac rif_nac" 
		print e

	#mycountry = self.get_argument("thecountry");
	mystate = self.get_argument("thestate");
	mycity = self.get_argument("thecity","");
	
	print "..............mycity"
	print mycity
	print "..............mycity"
	

        print self.request.arguments
        myfieldscompany = ""
        
        myhascompany = "false"
        mynamecompany = "none"
        myrifcompany = "none"
        mydircompany = "none"
        
        if self.request.arguments.has_key("hascompany"):
	      myhascompany = self.get_argument("hascompany")        	    
	      mynamecompany = self.get_argument("companyname")                
	      myrifcompany = self.get_argument("rif")
	      mydircompany = self.get_argument("companydir")
        
        if myhascompany == "true":
	  myfieldscompany = "es_empresa:%s nombre_empresa:%s rif_empresa:%s direccion_empresa:%s"  % (myhascompany,mynamecompany,myrifcompany,mydircompany)
	  
	myfieldsaddress =" Estado:%s Ciudad:%s" % (mystate,mycity)



        myip = self.request.remote_ip
        if (myip == "::1"):
            myip = "localhost"


        myfullname  = u"%s %s" % (myfirstname,mylastname)

        print myfullname

        myemail = self.get_argument("email")

        myone = self.get_argument("passwordone")
        mytwo = self.get_argument("passwordtwo")
        
        myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH) 
	myinflow.setHostURL(safetconfig.SERVER_URL)


        resultstr = u""
        myticket = ''.join(random.choice('abcdef0123456789') for _ in range(40))

	loader = tornado.template.Loader(os.path.join(MYHOME,"templates"))        
	
	myoperation = QString(u"operacion:agregar_usuario  cuenta:%s email:%s nombres:%s apellidos:%s cedula:%s %s ip_origen:%s %s %s %s %s" % (myaccount,myemail,myfirstname, mylastname,myci,myrif,myip,myfieldsaddress,myfieldscompany,mycinac,myrifnac)  )      
	
	#print u"myoperation" + myoperation.encode("utf-8")
        
                
        isinserted = myinflow.toInputForm(myoperation)

        print "isinserted:|%s|" % (isinserted)
        
        
        if isinserted != "Ok":
            mystr = u"%s" % (myinflow.currentError())
            self.write(loader.load("message.html").generate(mymessage=mystr))
            return

        resultstr = u"%s" % ( myinflow.checkUserRegister(myfullname,myaccount,myemail,myone,mytwo,myticket) ) 


        self.write(loader.load("message.html").generate(mymessage=resultstr))



def checkPermise(mypermise, current_user, current_pass):
	myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)         
        result = myinflow.login(current_user,current_pass)    
        if not result:
	       print "error checkPermise auth"
	       myinflow.log("error checkPermise auth")
	       
	       return 0
	       

	print "********************...myperms mypermise: |%s|" % (mypermise)       
       	myperms = myinflow.doPermiseOperation(mypermise)
	print "********************...myperms %d" % (len(myperms))
	currperm = u"%s" % myperms[QString("execute")]
	
	print "********************...myperms:"
	user_perm = 1
	
	if (currperm == "true"):	  
	      return 1
	return 0
	
        

        
        
        
class GoChangePassHandler(tornado.web.RequestHandler):
     def get(self,name_user):
        current_user = self.get_secure_cookie("user")
        current_pass = self.get_secure_cookie("pass")
        
        if current_user==None or len(current_user) == 0:
	    print "*************"
	    print "Current user is EMPTY"
	    current_user="invitado"
	    current_pass="clavecomprador"	    
	    self.set_secure_cookie("user", current_user)
	    self.set_secure_cookie("pass", current_pass)

	mynameuser = name_user
        if mynameuser == "none":
	    mynameuser = current_user
	
	myoperation = u"operacion:Listar_datos Cargar_archivo_flujo: " + safetconfig.HOMESAFET_PATH + "/.safet/flowfiles/usuarioscuenta.xml Variable: vTodas parameters.ByAccount:" + mynameuser   
	myinfo = getUserInfo(current_user,current_pass,myoperation)
	print "myinfo:" + myinfo

	myoperation = u"operacion:Listar_datos Cargar_archivo_flujo: "+safetconfig.HOMESAFET_PATH + "/.safet/flowfiles/tendencias_sub.xml Variable: vPorCategoria"
	mytrendings = getUserInfo(current_user,current_pass,myoperation)

	myoperation = u"operacion:Listar_datos Cargar_archivo_flujo: "+safetconfig.HOMESAFET_PATH + "/.safet/flowfiles/subcategorias.xml Variable: vTodas"
	mysubs = getUserInfo(current_user,current_pass,myoperation)

        
        myoperation  = u"operacion:Listar_datos  Cargar_archivo_flujo: /home/vbravo/.safet/flowfiles/anuncios.xml Variable: vTodas"
        myanuncios = getUserInfo(current_user,current_pass,myoperation)
        #print "myanuncios:" + myanuncios
        
        
      
        
	loader = tornado.template.Loader(os.path.join(MYHOME,"templates"))  
        self.write(loader.load("changepass.html").generate(ads = myanuncios, subs = mysubs, trendings = mytrendings, user_id = 1,name_operation = "All", current_user = current_user, user_info = myinfo, cities = [], boxsearch = "none",profile = "Victor Profile") )
        
     def post(self,name_user):
       
        current_user = self.get_secure_cookie("user")
        current_pass = self.get_secure_cookie("pass")
        loader = tornado.template.Loader(os.path.join(MYHOME,"templates"))  
        
        if current_user==None or len(current_user) == 0:
	    print "*************"
	    print "Current user is EMPTY"
	    self.write(loader.load("message.html").generate(mymessage=u"No está autenticado. No puede ingresar a esta página."))
	    return
	    
        myoperation = u"operacion:Listar_datos Cargar_archivo_flujo: " + safetconfig.HOMESAFET_PATH + "/.safet/flowfiles/usuarioscuenta.xml Variable: vTodas parameters.ByAccount:" + current_user   
	myinfo = getUserInfo(current_user,current_pass,myoperation)
	user_id = json.loads(myinfo)[0]["id"]
	    
        oldpass = self.get_argument("oldpass").strip()
        pass1 = self.get_argument("pass1").strip()
        pass2 = self.get_argument("pass2").strip()
        if oldpass != current_pass:
	    self.write(loader.load("authmessage.html").generate(mymessage=u"La contraseña anterior no coincide.",current_user = current_user, user_id = user_id))
	    return
        if pass1 != pass2:
	    self.write(loader.load("authmessage.html").generate(mymessage=u"La nueva contraseña y su repetición no coinciden.",current_user = current_user, user_id = user_id))	    
	    return
	    
	    
	  
        
        print "oldpass:" + oldpass
        print "pass1:" + pass1
        print "pass2:" + pass2
        
        myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH) 
        
        result = myinflow.login(current_user,current_pass)
        print "GoChangePassHandler result login:%d" % (result)
        
	myaction = u"%s" % ("operacion:Modificar_usuario Nombre_cuenta_usuario:%s Contrasena_usuario:%s" %  (current_user,pass1)  )
	
	print "GoChangePassHandler action:|%s|" % (myaction)
        result = myinflow.toInputUsers(myaction)
 
        
        print "GoChangePassHandler result action:%d" % (result)
        if not result:        
	    self.write(loader.load("authmessage.html").generate(mymessage=u"Ocurrió un fallo al intentar cambiar la contraseña.",current_user = current_user, user_id = user_id))
	    return
	    
	
	self.write(loader.load("authmessage.html").generate(mymessage=u"Contraseña fue cambiada satisfactoriamente.",current_user = current_user, user_id = user_id))
        





settings = dict(
            static_path=os.path.join(MYHOME, "static"),
            cookie_secret="32oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            login_url="/auth/login",
            
            google_oauth= {
                'key': 'client_id',
                'secret': 'client_secret',
                'redirect_uri': safetconfig.SERVER_URL + 'login/google',
                'scope': ['openid', 'email', 'profile']
            },
            twitter_consumer_key= '5H74LPWThxV6HfgEEETdO7XBA',
            twitter_consumer_secret= 'vuj9kHkPOLwDm3PTaaTlhGl15YARGryw9PSoUXf25TYIjhjUwj',
           )


class GoFormHandler(tornado.web.RequestHandler):    
    def get(self,name_template,name_operation,currid,currmessage=None):                    
    
        #print "mycurrid:|%s|" % (currid)
        current_user = self.get_secure_cookie("user")
        current_pass = self.get_secure_cookie("pass")
	title = name_operation.replace("_"," ")
     
         
      
      
        myoperation = u"%s" % (tornado.escape.url_unescape(name_operation) )
        
        themessage = None
        if currmessage != None and currmessage == "success":
	  themessage = "Se  enviaron los datos correctamente"

	#print "currmessage:|%s|" % (currmessage)
	#print "the message:%s" % (themessage)
        #print "myoperation:%s" % (myoperation)
        
        ori_template = name_template
        
        loader = tornado.template.Loader(os.path.join(MYHOME,"templates"))        
        if not current_user:
	    print "loader.1"
            self.write(loader.load("message.html").generate(mymessage=u"No está autenticado. No puede ingresar a esta página."))
            return        

        #print "current_user: %s"  % (current_user)
        #print "current_pass: %s"  % (current_pass)
        
        

        current_html = getForm(current_user,current_pass,myoperation,currid,ori_template)
	#print current_html
        
        modify_html = ""
        print "GoForm...pubs...2...***name_template:|" + name_template + "|"
          
	print "GoForm...pubs...3...***name_template:|" + name_template + "|" 


	menues = menuToList("/goform/addgeneric",current_user,current_pass)

 
        try:
	        mytemplate = u"%s.html" % (name_template)
	
		self.write(loader.load( mytemplate ).generate(current_user = current_user,mycode= current_html, title = title, user_id = "1", menues = menues))
		print "GoForm...4"
	except Exception as e:
		print "exceptioni**:"
		print e
 

def menuToList(prefix, current_user,current_pass):
  	minit = initializeItemMenu(current_user,current_pass)
	print "=" * 80	
	print ""
	menues  = {}

	newentry = ""		
	
	for n in minit["actions"]:
	      for i in n["items"]:
		      if len(i["href"]) > 0:
			  myaction = i["href"][1:]
			  #print "action:" + myaction
			  menues[ myaction ] = 	 u'<li><a href="%s%s/0">%s</a></li>' % (prefix, i["href"],i["action_name"])

	
	return menues
	
	
	
	#menues["agregar_empleado"] =  generateItemMenu("agregar_empleado",minit,current_user,current_pass)
	#print ""
	#menues["Modificar_solicitud_vacaciones"] =  generateItemMenu("Modificar_solicitud_vacaciones",minit,current_user,current_pass)
	
	print "=" * 80
  
  

def initializeItemMenu(current_user,current_pass):
      myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
      myinflow.setHostURL(safetconfig.SERVER_URL)     
      myinflow.setHostMediaPath(safetconfig.MEDIA_URL)
      myinflow.setInputPath(safetconfig.HOMESAFET_PATH + "/.safet/input/deftrac.xml")


      result = myinflow.login(current_user,current_pass)    

      if not result:
	      print "error from authentication"
	      return []
	    
      menues = []		
      try:
	
	mymenu =  u"%s" % (myinflow.menuCommands())
	menues = json.loads(mymenu)
      except Exception as e:
	    print "Exception JSON initializeItemMenu"
	    print "e"
	    print "---------------------------------"

      return menues

	
      
    

		      
		
    
  

class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        #print "Logout"
        self.clear_cookie("user")
        self.clear_cookie("pass")
        self.clear_cookie("ticket")
        loader = tornado.template.Loader(os.path.join(MYHOME,"templates"))        
        self.write(loader.load("login.html").generate(mymessage=False))


class GeneratePdfParametroHandler(tornado.web.RequestHandler):
    def post(self):
        loader = tornado.template.Loader(os.path.join(MYHOME,"templates"))
        current_user = self.get_secure_cookie("user")
        current_pass = self.get_secure_cookie("pass")
        
	print "GeneratePdfParametroHandler...1"
	id_form = self.get_argument("id_form")
	print "GeneratePdfParametroHandler...2...id_form:|%s|"  % (id_form)

        menues = menuToList("/goform/addgeneric",current_user,current_pass) 

        try:
            myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
            result = myinflow.login(current_user,current_pass)
            myconsult = u"operacion:Listar_datos Cargar_archivo_flujo: "+ safetconfig.HOMESAFET_PATH +"/.safet/flowfiles/SolicitudVistaVacaciones.xml Variable: vSolicitud parameters.ByPeriod:"+id_form+""
	    print myconsult
            result = myinflow.toInputConsole(myconsult)  
            myjson = u"%s" % (myinflow.currentJSON())	    

            mypubs = json.loads(u"%s" % (myjson) )["safetlist"][0]
	    print "mypubs"
	    print mypubs

            print "nombres_suplente_1: %s" % (mypubs['nombres_suplente_1'])
            name_file = 'planilla.pdf'
            render_to_pdf(mypubs,name_file)
            self.write(loader.load("generatepdfParameter.html").generate(error = "",mymessage=False,current_user='vbravo', name_file = name_file,user_id=1, menues = menues))            
            
        except Exception as e:
	    print "Exception: "
	    print e
            self.write(loader.load("generatepdfParameter.html").generate(error = "Usuario no existe...??",mymessage=False,current_user='vbravo',user_id=1, menues = menues))
	
	return



class GeneratePdfHandler(tornado.web.RequestHandler):
    """
       Permite generar el pdf solo del usuario logueado
    """
    def get(self):
        loader = tornado.template.Loader(os.path.join(MYHOME,"templates")) 
        current_user = self.get_secure_cookie("user")
        current_pass = self.get_secure_cookie("pass")

	safet_data = []
	
	menues = menuToList("/goform/addgeneric",current_user,current_pass)
		

	try:     
	        myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
	        result = myinflow.login(current_user,current_pass)

		myconsult = u"operacion:Listar_datos Cargar_archivo_flujo: /home/vbravo/.safet/flowfiles/SolicitudVistaVacacionesUser.xml Variable: vTalentoHumano"
		myinflow.toInputConsole(myconsult)  
        	myjson = u"%s" % (myinflow.currentJSON())
        	safet_data = json.loads(u"%s" % (myjson) )["safetlist"]
	except Exception as e:
		print "GeneratePdfException"
		print e
		print "=" * 80

   
	print "get...GeneratePDfHandler...1"        
        self.write(loader.load("generatepdf.html").generate(safet_data=safet_data,mymessage=False,current_user='vbravo',user_id=1, menues = menues))
      
    

	
class GoLoginHandler(tornado.web.RequestHandler):
    def get(self):            
        #print "GoLoginGet"
        current_user = self.get_secure_cookie("user")
        current_pass = self.get_secure_cookie("pass")
        
	if current_user!=None and current_user!="invitado":
		self.redirect("/logout")		    
		return
		

        resultstr = safetconfig.SAFETREGISTER
        loader = tornado.template.Loader(os.path.join(MYHOME,"templates"))        
        self.write(loader.load("login.html").generate(mymessage=False))

    def post(self):       
        print "GoLoginPost...................1" 
        myuser = self.get_argument("account")
        mypass = self.get_argument("passwordone")


        myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH) 

        loader = tornado.template.Loader(os.path.join(MYHOME,"templates")) 
        myinflow.registerLogin(myuser)
        result = myinflow.login(myuser,mypass)

	myinflow.log("TRY_LOGIN: " + myuser)

        if not result:
            self.write(loader.load("login.html").generate(mymessage=True))
	    myinflow.log("TRY_LOGIN_NOVALID: " + myuser)
            return


	myinflow.log("TRY_LOGIN_SUCCESS: " + myuser)
        #print "auth user: |%s|" % (myuser)

        self.set_secure_cookie("user", myuser)
        self.set_secure_cookie("pass", mypass)
      
      
	if True:
		self.redirect("goform/addgeneric/Modificar_solicitud_vacaciones/0")		    
		return
      

 
        
class ProcessAjaxFormHandler(tornado.web.RequestHandler):    
	def post(self,name_operation):
	 #    print ".........ProcessAjaxFormHandler........post:" + name_operation
	    print "AjaxForm................1*"
	    current_user = self.get_secure_cookie("user")
	    current_pass = self.get_secure_cookie("pass")

	    print u"AjaxForm................1.....current_user:|%s|" % (current_user)
	    
	    if current_user==None or current_user=="invitado":
		self.write("{ \"message\": \"user unauthorized\", \"error\": \"True\" } ")
		return

	    
	    #print "current_user:" + current_user
	    
	      
	    print "AjaxForm................2"
	    print "AjaxForm................update.1"
	    myoperation = QString(u"operacion:%1 ").arg(name_operation)
	    
	    #print "file: %d" %( len(self.request.files) )
	    currfile = ""
	    filefield = " Foto:"
	    urlfile = safetconfig.MEDIA_PATH
	    urlfile = urlfile.replace(":","__SAFETCOLON__")
	    for myfile in  self.request.files.keys():
		      #print "key: %s " % (myfile)
		      for f in  self.request.files[myfile]:
			    #print u"  filename: %s " % (f["filename"])
			    #print u"  content_type: %s " % (f["content_type"])
			    currfile = u"%s/static/media/%s" % (MYHOME, 
f["filename"])
			    urlfile = urlfile + "/" + f["filename"]
			    #print currfile
			    filefield = filefield + urlfile + " "
			    thefile = open(currfile,"wb")
			    thefile.write(f["body"])
			    thefile.close()
	    #print "**---------------self.request.arguments:|%d|" % (len(self.request.arguments))
	    for item in self.request.arguments:
	          #print "item: %s" % (item)
		  myvalue = tornado.escape.to_unicode(self.get_argument(item))
		  #print "item: %s" % (myvalue)
		  myfield =QString(u" %1:%2").arg(item).arg(myvalue.replace(",","##SAFETCOMMA##"))
		  if not item.startswith("safet"):
			  if len(myvalue) > 0:
			    myoperation = myoperation + myfield
	    filefield.strip()
	    if filefield != " Foto:":
	      myoperation = myoperation + filefield
	    myoperation = myoperation.trimmed()
	    
		
	    print "AjaxForm................3"

	    myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
	    result = myinflow.login(current_user,current_pass)		
#	    print u"**********......operation(->):\n |%s|\n\n" % (myoperation)
	    #isinserted = myinflow.toInputForm(myoperation )
	    
	    
	    print "AjaxForm................4"
	    print "****AjaxForm................4...name_operation:" + name_operation
	    myconfkey = u" configurekey.Email/email.template.1: Estimado, {#nombres_repre}<br/> le enviamos la boleta de su representado <b>{#nombres_alumno}</b> para el 2do Lapso. <br/><br/> Lo podrá descargar desde la sección de este correo. <br/><br/> Muchas gracias por su atención. "

	    if name_operation.endswith("boleta_por_correo"):
		print "...ending por_correo"
		myoperation = myoperation + myconfkey
		print "...por_correo:%s" % (myoperation)


	    print "AjaxForm................myoperation:|%s|" % (myoperation)
	    

	    isinserted = myinflow.toInputForm(myoperation )	    	    
	        
	    
	    print "AjaxForm................5....isinserted:" + isinserted
	    	    
	    if not isinserted:
	      
		myerror = u"%s" % (myinflow.currentError())
		#print u"error:%s" % (myerror)
		
		self.write(u'{ "error": "%s" }' % (myerror) )		
		return
	    
	    myjson = u"%s" % (myinflow.currentJSON())
	   
	    currpostaction = myinflow.postAction()
	    myinflow.log("....PROCESSING POSTACTION1") 
	    if len(currpostaction) > 0:
			allpost = "%s".strip() %  (currpostaction)
                	postlist = allpost.split("##SAFETSEPARATOR##")
			for currpost in postlist:
				presult = myinflow.toInputForm(currpost,False)
				myinflow.log("PRESULT POSTACTION RESULT:" + presult)


	    print "AjaxForm................6"
	    #print "myjson: %s" % (myjson)
	    self.write(myjson)
		
		
		
		
	def getForm(self,current_user,current_pass,name_operation):
	    myinflow = Safet.MainWindow(safetconfig.HOMESAFET_PATH)
	    myinflow.setHostURL(safetconfig.SERVER_URL)     
	    myinflow.setHostMediaPath(safetconfig.MEDIA_URL)
	    myinflow.setInputPath(safetconfig.HOMESAFET_PATH + "/.safet/input/deftrac.xml")

	    result = myinflow.login(current_user,current_pass)    
	    #print  "result:%d"  % (result)
	    #selurl = u"/deftrac:operacion:modificar_usuario"
	    
	    selurl = u"/deftrac:operacion:%s" % (name_operation)	    
	    
	    #print "selurl:|%s|" % (selurl)
	    	    
	    html1 = unicode(myinflow.generateFormHead(selurl))  
	    
	    html2 = unicode(myinflow.menuForm(selurl))                

	    html3 = unicode(myinflow.generateFormFooter(selurl))
	    
	    current_html = html1 + html2 + html3
	    
	    #print "getForm ...(end)"
	    return current_html


	    



mycontroller = [           
            (r"/", GoLoginHandler),
            (r"/register", RegisterHandler),
            (r"/checkaccount", CheckAccountHandler),
            (r"/checkci", CheckCIHandler),     
            (r"/loaddata", LegacyLoadDataHandler),            
            (r"/checkrif", CheckRIFHandler),
            (r"/gologin", GoLoginHandler),
            (r"/generatepdf/", GeneratePdfHandler),
            (r"/generateformpdf/", GeneratePdfParametroHandler),            
            (r"/ajaxconsole", ProcessAjaxConsoleHandler),
            (r"/logout", LogoutHandler),
            (r"/goregister", GoRegisterHandler),
	    (r"/listar/([^\s]+)/([^\s]+)", ListHandler),
            (r"/cargarboletas/", LoadScoreHandler),
            (r"/procesararchivos_([^\s]+)", ProcessFilesHandler),           
	    (r"/forma_([^\s]+)/([^\s]+)/(\d+|none)", ProcessFormHandler),
            (r"/goform/([^\s]+)/([^\s]+)/(\d+|none)/?([^\s]*)", GoFormHandler),    
	    (r"/ajaxforma_([^\s]+)", ProcessAjaxFormHandler),       
            (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': "/home/vbravo/github/boletas/boletas/static"}),
        ]


class Application(tornado.web.Application):
   def __init__(self):
       settings = {
           'static_path': os.path.join(MYHOME, "static"),
           'cookie_secret': "32oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
           'login_url': "/auth/login",
            
           'google_oauth': {
               'key': 'client_id',
               'secret': 'client_secret',
               'redirect_uri': 'http://localhost:8080/login/google',
               'scope': ['openid', 'email', 'profile']
           },
           'twitter_consumer_key': '5H74LPWThxV6HfgEEETdO7XBA',
           'twitter_consumer_secret': 'vuj9kHkPOLwDm3PTaaTlhGl15YARGryw9PSoUXf25TYIjhjUwj',
           'google_oauth': {
               'key': '572851633771',
               'secret': '7Hhn4WXM7RQHaildm0n0aOjv'
           }
       }
       print os.path.join(MYHOME, "static")

       handlers = mycontroller
        
       tornado.web.Application.__init__(self, handlers, **settings)


def main():
   tornado.options.parse_command_line()
   http_server = tornado.httpserver.HTTPServer(Application())
   http_server.listen(options.port)
   tornado.ioloop.IOLoop.instance().start()



if __name__ == "__main__":
   main()



