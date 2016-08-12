# -*- coding: utf-8 -*-

import ho.pisa as pisa
from planilla_pdf import Plantilla_HTML
import os


def render_to_pdf(mydata,nombre_archivo):
    """
    Conviente la respuesta en un archivo pdf
    """    
    try:
            
        html = Plantilla_HTML(mydata)
        pdfFile = file(nombre_archivo, "wb")
        pdf = pisa.CreatePDF(html,pdfFile)
        pdfFile.close()
                
        os.system("rm static/tmp/Planilla_Vacaciones.pdf")
        os.system("mv Planilla_Vacaciones.pdf static/tmp/")
        
        return True
    except:
        return False
    
  


