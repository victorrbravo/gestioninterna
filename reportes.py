# -*- coding: utf-8 -*-

from xhtml2pdf import pisa
import cStringIO as StringIO

from planilla_pdf import Plantilla_HTML
import os


def render_to_pdf(mydata,nombre_archivo):
    try:
        print "render 1"    
	#html = u""
        html = Plantilla_HTML(mydata)

	result = StringIO.StringIO()

	pdf = pisa.pisaDocument(StringIO.StringIO(html), dest=result)                
        
	if not pdf.err:
		myfile = open("test.pdf","w")
		myfile.write(result.getvalue())

		myfile.close()
		print "no error...ok!"
		return True

        return False
    except Exception as e:
	print "PDF exception"
	print e
        return False
    
  


