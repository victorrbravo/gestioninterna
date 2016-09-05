

import Safet

myinflow = Safet.MainWindow("/home/vbravo")

myinflow.login("vbravo","zpinquar")

#op ="operacion:agregar_representante_alumno n_lista:1 grado_seccion:2A nombres_alumno:Paola apellidos_alumno: Alvarado nombres:Morela apellidos: Briceno ci: 12780989 correo:morelabfa@hotmail.com esta_solvente:solvente"


lines = [line.rstrip('\n') for line in open('lista_empleados.txt')]
for op in lines:
	print "\n..."
	print op
	result = myinflow.toInputForm(op)
	print "result"
	print result

