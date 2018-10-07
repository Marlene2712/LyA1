def em():
    email=input("Ingresar Email: ")
    
    if "@" in email:
        Correo=email.split('@')
        usuario=Correo[0]
        desa=Correo[1]
        
        if "." in desa:
            txfin=desa.split('.')
            os=txfin[0]
            extencion=txfin[1]
            
            print ("El email " +  email +" es valido")
        
        else:
            print ("El email " +  email +" no es valido")
        
    else:
        print ("El email " +  email +" no es valido")

from time import time
start =time()
em()
end=time()-start
print(end)