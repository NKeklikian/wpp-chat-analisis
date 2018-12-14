import pandas as pd
from collections import defaultdict

a = open("salida.txt")

droga = defaultdict(int)
lineas_x_persona = defaultdict(list)
l_x_anio = defaultdict(int)

for linea in a:
	vale = ":" in linea
	for e in ["changed", "Bonifacio 1590", "Messages to", "9 11 3152", "added", "created", "left"]:
		vale = vale and (e not in linea)
	if vale:
		try :
			persona = linea.split(":")[1].split("- ")[1]
			anio = linea.split("/")[2].split(",")[0]
			mes = linea.split("/")[0]
			l_x_anio[mes+"-"+anio] += 1
			lineas_x_persona[persona].append(linea.split(":")[2])
			linea = linea.lower()
			es_droga = False
			for p in ["maria","droguita","cogo","falopa","cocuchi","merca","lsd","pepa","peponia","movida","flor","droga","cannabis","porro","porrito","marihuana","faso"]:
				es_droga = es_droga or (p in linea)
			droga[persona] += es_droga
		except :
			pass

for i,j in sorted([(i,droga[i]) for i in droga], key=lambda x:x[1], reverse=True):
	print i, j
#	if False:
#		try :
#			if "1" in linea.split(":")[2] and "sado" in linea:
#				print linea
#				raw_input()
#		except :
#			pass
#	if linea[0] in list(map(str,range(10))) and linea[1] == " ":
#		print linea
#		raw_input()
a = open("salida.txt")

l = [(i, l_x_anio[i]) for i in l_x_anio]
print sorted(l,key=lambda x: 100*int(x[0].split("-")[1]) +int(x[0].split("-")[0]) )

act, sig = "", ""
candidatos = []
while a:
	sig = act
	act = a.readline()
	if act == "":
		break
	lineas = []
	while ":" not in act and act != "":
		lineas.append(act)
		act = a.readline()
	if lineas:
		candidatos.append((sig, lineas))

cand_asado = []

for i,j in candidatos:
	if "Viernes" in i or "asado" in i.lower() or "carne" in i.lower() or "chimi" in i.lower() or "costillar" in i.lower():
		cand_asado.append((i,j))
print len(candidatos)
print len(cand_asado)
#for i in cand_asado:
#	print i
#	raw_input()


cant_x_pers = [(persona, len(lineas_x_persona[persona])) for persona in lineas_x_persona]
cant_x_pers.sort(key = lambda x: x[1], reverse = True)
for i, j in cant_x_pers:
	print i,j
	palabras = defaultdict(int)
	saltear = ["que","de","la","a","el","no","en","y","un","es","se","Yo","yo","una","con","Y","los","si","No"
	,"por","con","para","Jajaja","pero","como","estoy","Si","El","hay","mi","esta",
	"te","le","o","Pero","las","lo","mas","Que","me","del","Jaja","Jajajajaja","tu","al",
	"este","De","eso","La","Es","A","Me","Jajajaja","Jajajajajaja","En","Por","Para","Como"]
	for l in lineas_x_persona[i]:
		for p in l.strip("\n").split():
			if p not in saltear:
				palabras[p] += 1
	pares = [(p,palabras[p]) for p in palabras]
	pares.sort(key = lambda x: x[1], reverse = True)
	#print pares[:20]
