# -*- coding: utf-8 -*-

a = open("Chat.txt")
s = open("salida.txt","w")

for linea in a:
	limpia = linea
	for x, y in [["\xc3\xa1","a"],["\xc3\xa9","e"],["\xc3\xad","i"],["\xc3\xb3","o"],["\xc3\xba","u"],["\xc3\xb1","ni"]]:
		limpia = limpia.replace(x,y)
	s.write(limpia)

print "done"