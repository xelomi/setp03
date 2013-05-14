#marcelo Minay
#Realizar una función que determine la cantidad de veces que se repite las palabras en un texto y mostrar por pantalla

#Realizar una función recursiva que cuente la cantidad total de palabras que contiene un archivo

import re   # modulo contiene popitem
import sys		#modulo que contiene una función que permite aumentar la cantidad de veces que se realiza una recursión

sys.setrecursionlimit(999999)		#aumenta las veces que se realizan las llamadas recursivas.

def cuenta_palabras(diccionario):
	if (len(diccionario)==0):
		return(0)
	else:
		palabra,veces=diccionario.popitem()
		return(cuenta_palabras(diccionario)+int(veces))
      
diccionario_texto={} #Se genera el diccionario vacio para ser llenado

archivo=open('funes.txt',encoding='utf-8') #Archivo abierto
texto=archivo.read()   #guarda todo el texto en forma de String en la variable "texto"
archivo.close()         #cierra el archivo
texto=texto.lower()   #Deja el string solo con minisculas
lista_texto = texto.split()   #Genera una lista con todas las palabras, incluso repetidas
diccionario_texto = dict.fromkeys(lista_texto,0)  #crea un diccionario a partir de la lista previamente creada, cada valor asociado al key del diccionario es inicializada con el valor 0

#Recorre la lista con las palabras del texto
for i in lista_texto:

    #Si la palabra que está en la lista se encuentra en el diccionario se suma 1 al valor de la respectiva 'key' en el diccionario
    if i in diccionario_texto:
        diccionario_texto[i] = int(diccionario_texto[i]+1)

#Se crea una lista que contiene tuplas de cada 'key' del diccionario con su respectivo valor, ordenadas por su valor de mayor a menor
from operator import itemgetter
diccionario_listo=sorted(diccionario_texto.items(), key=itemgetter(1), reverse=True)  #reverse ordena las palabras de mayor a menor

#Imprime la lista de tuplas ya ordenada


for i in diccionario_listo:
    print(i)

print("La cantidad de palabras es:",cuenta_palabras(diccionario_texto))    #imprime la cantidad de palabras que contiene el archivo
