import random

def clase1():
    alfabeto=input("ingresa alfabeto")
    n=5
    m=0
    letra=""
    lista=[]
    
    while  m<=n:#checa que la cantidad de letras sea menor
        for x in range (0,len(alfabeto)): #avanza cada una de las letras del alfabeto
          
            letras=random.randint(1,5) #una letra aleatoria del alfabeto 
            letra=letra.join(random.choice(alfabeto)for _ in range(letras))#en cada vuelta se vaya realizando se agregara una letra 
        
            lista.append(letra)#append guarda
            letra="" #elimina la cadena que se tenia guardada dejandola vacia para que ingrese
            # una nueva si no se vacia la cadena se ara mas grande lo cual si son muchas combinaciones puede trabar la computadora 
            m=m+1  
    
    print (lista)#imprime la lista 

from time import time#tiempo que tardo en compilar 
start =time()
clase1()
end=time()-start
print(end)
