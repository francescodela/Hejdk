class Coche ():
    largoDelChasis= 250 
    AnchoDelChasis  = 120 
    ruedas = 4 
    encendido  = False 
    
    def  encender   (self):
        self.encendido = True  
        
    def estado (self) :
        if(self.encendido):
            return "el coche esta encendido "
        else :
            return  " el coche esta apagado "
coche = Coche ()
print ( "El largo del chasis es de : ",  coche.largoDelChasis )
print ("El ancho del chasis es de : ", coche.AnchoDelChasis)
print (f"tiene :  {coche.ruedas} ruedas "  )

coche.encender ()        
print (coche.estado())
        