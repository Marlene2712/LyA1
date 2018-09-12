def clase2():
    lista=input("escribe una cadena de texto")#input para que se pueda obtener texto escrito por el teclado
    cadena=""
    lista2=[]#lista donde se guardaran los valores que se imprimiran
    for i in (lista): #es cada uno de los valores de la lista
        m=i #toma el primer valor
        for x in (m): #primer valor 
            if x not in lista2:#not in separa los valores de el primer valor 
                lista2.append(x)#si el elemnto todavia no se encuentra en la lista se guarda 
                
    print (lista2)#se iempime la lista             
   
from time import time #es el que tomara el tiempo en que tarda en ejectutarce 
start =time()
clase2()
end=time()-start
print(end)   