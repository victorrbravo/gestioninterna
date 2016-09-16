# -*- coding: utf-8 -*-

def Plantilla_HTML(mydata):
    print "plantilla..1"
    HTML = """    
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
    <html>
        <head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8" />	
        <title>Planilla de Vacaciones</title>
            <style type="text/css">
                @page {
                    size:LETTER;
                    margin: 2cm;
                    @frame footer {
                        -pdf-frame-content: footerContent;
                        bottom: 1cm;
                        margin-left: 2cm;
                        margin-right: 2cm;
                        height: 2cm;
                    }
                }
            td{
            padding: 0 1 1 1;
            }
            </style>
        </head>
        <body>
        <center><img SRC="static/logo_planilla_vacaciones.png" NAME="graficos" WIDTH=514 HEIGHT=32 ></center>
         <P ALIGN=CENTER ><FONT COLOR="#000080" style="font-size: 12pt"><B>SOLICITUD DE VACACIONES</B></FONT></P>
        <br>
        <table width="100%"  cellspacing="0" cellpadding="5" >
        <tr>
            <td STYLE="border: 1px solid #000000;" COLSPAN=2 width="50%" align="left">
            SOLICITUD Nº:    
            """
    HTML += str(mydata['id'])       
    HTML += """
            </td>
            <td STYLE="border: 1px solid #000000;" COLSPAN=3 width="50%" align="left" >
               FECHA DE LA SOLICITUD: 
        """
    
    HTML += str(mydata['fechasolicitud'])[:10]
    
    HTML +="""  
            </td>
        </tr>
        <tr>
            <td STYLE="border: 1px solid #000000;" width="40%"  align="left"  >
            APELLIDOS Y NOMBRES: 
        """
    HTML += str(mydata['nombreapellido'])
    HTML += """  
            </td>                    
            <td STYLE="border: 1px solid #000000;" COLSPAN=3  align="left" >
            CEDULA DE IDENTIDAD: 
        """
    HTML += str(mydata['id_cedula'])
    HTML += """  
            </td>
            <td STYLE="border: 1px solid #000000;" align="left" width="20%" >
            FECHA DE INGRESO: 
            <br/>
        """
    print "plantilla..6.1 %s" % (mydata['fecha_ingreso'][:10])
    HTML += str(mydata['fecha_ingreso'][:10])
    print "plantilla..7"
    HTML +="""  
            </td>
        </tr>
        <tr>
            <td STYLE="border: 1px solid #000000;"  COLSPAN=3  align="left">
               CARGO:   
        """
    HTML += str(mydata['cargo'])
    HTML +="""  
            </td>                    
            <td  STYLE="border: 1px solid #000000;" COLSPAN=2  align="left">
            DEPENDENCIA: 
        """
    HTML += str(mydata['departamento'])

    HTML += """  
            </td>                   
        </tr>
        </table>
        <br>
        <table width="100%"  cellspacing="0" cellpadding="5" >
        <tr>
            <td  STYLE="border: 1px solid #000000;" align="left">
            DÍAS SOLICITADOS:  
            """
    HTML += str(mydata['diassolicitados'])

    HTML += """ 
            </td>
            <td  STYLE="border: 1px solid #000000;" align="left">
            DIAS PENDIENTES:     
            """
    HTML += str(mydata['diasadicionales'])              
    
    HTML += """
            </td>
            <td  STYLE="border: 1px solid #000000;" align="left">
            PLANIFICACIÓN ESTIMADA:              
            """
    HTML += str(mydata['diasadisfrutar'])              
    
    HTML += """
            
            </td>    
        </tr>
        <tr>
            <td  STYLE="border: 1px solid #000000;" align="left">
            VACACIONES SOLICITADAS:
            <br>DESDE:
            """
    HTML += str(mydata['fechainicio'][:10])                  
    HTML += """
            
            <br>HASTA:
            """
    HTML += str(mydata['fechafin'][:10])                  
    HTML += """
            
            </td>    
            <td  STYLE="border: 1px solid #000000;" align="left">
            NÚMERO DE DÍAS HÁBILES
            """
    HTML += str(mydata['diassolicitados'])                  
    HTML += """            
            <br>
            <br> 
            </td>
            <td  STYLE="border: 1px solid #000000;" align="left">
            FIRMA DEL SOLICITANTE:
            <br>
            <br>
            <br> 
            </td>
        </tr>
        <tr>
            <td  STYLE="border: 1px solid #000000;" align="left">
              SUPLENTE(S):
            """
    HTML += str(mydata['nombres_suplente_1'])                  
    HTML += """                                    
            <br>            
            </td>	    
            <td  STYLE="border: 1px solid #000000;" align="left">
            CARGO(S) SUPLENTE(S):
            """
    HTML += str(mydata['cargo_suplente_1'])                  
    HTML += """                                    
            <br>            
            </td>
            <td  STYLE="border: 1px solid #000000;" align="left">
            FIRMA(S) SUPLENTE(S) INTERNO(S):
            <br>
            <br>            
            </td>
        </tr>	
        <tr>
            <td  STYLE="border: 1px solid #000000;" COLSPAN=2 align="left">
            FIRMA CARA VISIBLE: (o encargado de área para el caso de gestión interna)
            <br>
            <br>
            </td>	    
            <td  STYLE="border: 1px solid #000000;" align="left">
            FIRMA DIRECTOR DEL ÁREA: 
            <br>
            <br>
            </td>
        </tr>
        <tr>
            <td  STYLE="border: 1px solid #000000;" COLSPAN=2 align="left">
            FIRMA DIRECTOR DEL ÁREA: (De ser el caso)
            <br>
            <br>
            </td>	    
            <td  STYLE="border: 1px solid #000000;" align="left">
            FIRMA DIRECTOR DEL ÁREA (De ser el caso)
            <br>
            <br>
            </td>
        </tr>	
        <tr>
            <td  STYLE="border: 1px solid #000000;" COLSPAN=3 align="left">
            OBSERVACIONES:
            <br>
            </td>	    
        </tr>
        <tr>
            <td  STYLE="border: 1px solid #000000;" align="left">
            FIRMA ÁREA DE TALENTO HUMANO:
            <br>
            <br>
            </td>	    
            <td  STYLE="border: 1px solid #000000;" align="left">
            FIRMA DIRECCIÓN GESTIÓN INTERNA:
            <br>
            <br>
            </td>
            <td  STYLE="border: 1px solid #000000;" align="left">
            FIRMA DIRECCIÓN  EJECUTIVA:
            <br>
            <br>  		
            </td>
        </tr>	
        </table>
        <br>
        <table width="100%"  cellspacing="0" cellpadding="5" >
        <tr>
            <td   STYLE="border: 1px solid #000000; background-color: #D5D5D5; padding: 0 0 0 0;" COLSPAN=5 align="center">
            PARA SER LLENADO POR ÁREA DE TALENTO HUMANO:
            </td>
        <tr>
            <td  width="28%" STYLE="border: 1px solid #000000;" align="left">
            FECHA DE REINCORPORACIÓN:
            <br>
            <br>
            </td>	    
            <td  width="28%" STYLE="border: 1px solid #000000;" align="left">
            FECHA FINALIZACIÓN VACACIONES:
            <br>			    
            </td>
            <td COLSPAN=2 align="left">
            DÍAS HÁBILES A DISFRUTAR:
            <br>
            <br>	
            </td>
            <td width="16%" STYLE="border: 1px solid #000000;" align="left">
            DÍAS INHÁBILES:
            <br>
            <br>
            </td>	    
        </tr>
        <tr>
            <td  STYLE="border: 1px solid #000000;" align="left">
            DIAS ADICIONALES:
            <br>
            <br>	    
            </td>	    
            <td STYLE="border: 1px solid #000000;" align="left">
            BONO VACACIONAL:
            <br>
            <br>	    
            </td>
            <td  STYLE="border: 1px solid #000000;" COLSPAN=3  align="left">
            VACACIONES PENDIENTES PERÍODOS:
            <br>
            <br>	    
            </td>
        </tr>	
        <tr>
            <td  STYLE="border: 1px solid #000000;" align="left">
            FIRMA ÁREA DE TALENTO HUMANO
            <br>
            </td>	    
            <td  STYLE="border: 1px solid #000000;" COLSPAN=4 align="left">
            COMENTARIOS:
            <br>
            <br>
            </td>
        </tr>
        <tr>
            <td  STYLE="border: 1px solid #000000;" align="left">
            ENCARGADO(A) DE NÓMINA:
            <br>
            <br>	    
            </td>	    
            <td  STYLE="border: 1px solid #000000;" COLSPAN=2  align="left">
            FIRMA:
            <br>
            <br>	    
            </td>
            <td  STYLE="border: 1px solid #000000;" COLSPAN=2  align="left">
            FECHA:
            <br>
            <br>	    
            </td>	    
        <tr>
            <td   STYLE="border: 1px solid #000000; background-color: #D5D5D5; padding: 0 0 0 0;" COLSPAN=5 align="center">
            PARA SER LLENADO POR ÁREA DE FINANZAS
            </td>
        </tr>
        <tr>
            <td  STYLE="border: 1px solid #000000;" align="left">
            DÍAS HÁBILES A DISFRUTAR:
            <br>
            </td>	    
            <td  STYLE="border: 1px solid #000000;" COLSPAN=2 align="left">
            DÍAS INHÁBILES:
            <br>
            </td>
            <td  STYLE="border: 1px solid #000000;" COLSPAN=2 align="left">
            DÍAS ADICIONALES:
            <br>
            </td>
        </tr>
        <tr>
            <td  STYLE="border: 1px solid #000000;" align="left">
            BONO VACACIONAL:
            <br>
            <br>
            <br>	    
            </td>	    
            <td STYLE="border: 1px solid #000000;"  COLSPAN=2 align="left">
            VACACIONES A CANCELAR:
            <br>SUELDO DEL MES:
            <br>SUELDO ANTICIPADO:
            </td>
            <td  STYLE="border: 1px solid #000000;" COLSPAN=2 align="left">
            TOTAL A CANCELAR:
            <br>
            <br>
            <br>	    
            </td>
        </tr>	
        </table>	
        </body>
    </html>
    """
    return HTML
