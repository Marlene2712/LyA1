#https://www.lawebdelprogramador.com/codigo/Python/2040-Validar-cuenta-de-correo.html
def er():
    import re
     
    correo=input("Ingresar Email: ")
     
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
        print ("El Correo " + correo  + " es correcto")
    else:
        print ("El Correo " + correo  + " es incorrecto")

from time import time
start =time()
er()
end=time()-start
print(end)