from xhtml2pdf import pisa 
import cStringIO as StringIO 
     


html = ""
with open ("test.html", "r") as myfile:
    html=myfile.read()


result = StringIO.StringIO() 
pdf = pisa.pisaDocument(StringIO.StringIO(html), dest=result) 

if not pdf.err: 
	print "no error"
	myfile = file("test.pdf","wb")
	myfile.write(result.getvalue())
	myfile.close()


      
     
