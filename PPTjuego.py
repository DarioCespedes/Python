#Implementacion juego piedra, papel y tijeras
#Dario Andres Cespedes Amaya
import random
print( "            Bienvenido a Piedra vs Papel vs Tijeras")
print("================================================================")
opc="si"
pusuario=0
pmaquina=0
ronda=1

def playagain():
    opc=input("Desea jugar otra vez : si o no \n----- \n")
    opc=opc.lower()
    print ("----")
    
        
while(opc=="si"):
    
    opciones= ("piedra","papel","tijeras")
    maquina=random.choice(opciones)
    print("RONDA ", ronda)
    usuario= input("Digite su opción : * piedra * - * papel * - * tijeras * \n Opcion : " )
    usuario= usuario.lower()

    if( usuario == maquina ):
        print ("Es un empate")
    elif( usuario == "piedra" ):
        if (maquina == "tijeras" ):
            print ("El usuario gana")
            pusuario +=1
        elif(maquina == "papel"):
            print ("La maquina gana")
            pmaquina+=1
            
    elif( usuario == "papel" ):
        if (maquina == "piedra" ):
            print ("El usuario gana")
            pusuario +=1
        elif(maquina == "tijeras"):
            print ("La maquina gana")
            pmaquina+=1
            
    elif( usuario == "tijeras" ):
        if (maquina == "papel" ):
            print ("El usuario gana")
            pusuario +=1
        elif(maquina == "piedra"):
            print ("La maquina gana")
            pmaquina+=1  
   
    ronda+=1
    print("---- PUNTUACION ----")
    print("Puntuacion usuario : ",pusuario)
    print("Puntuacion maquina : ",pmaquina) 
    print("--------------------")          
    if (pusuario==3 ):
        print("El ganador definitivo es el usuario con 3 puntos")
        pusuario=0
        pmaquina=0
        ronda=1
        playagain()
    elif(pmaquina == 3):
        print("El ganador definitivo es la maquina con 3 puntos")
        pusuario=0
        pmaquina=0
        ronda=1
        playagain()
    
    
    
    
    