from tkinter import *
import random

raiz=Tk()
raiz.title("Juego de piedra papel y tijera")

frame=Frame(raiz,width=500,height=500)
frame.config(bg="grey")
frame.pack()

mano_jugador=""

mano_maquina=""

mensaje=""
mensaje2=""

mensaje_impreso1=StringVar()
mensaje_impreso2=StringVar()

#----------------función que cambia la variable mano--------------
def eleccion(mano):
	global mano_jugador
	mano_jugador=mano

#------------------- elección aletaoria de la maquina--------------

def jugar():
	global mano_maquina
	global mensaje
	global mano_jugador
	h=random.randint(0,2)
	if h==0:
		mano_maquina="piedra"
		mensaje2="La maquina ha elegido piedra"
	elif h==1:
		mano_maquina="papel"
		mensaje2="La maquina ha elegido papel"
	else: 
		mano_maquina="tijera"
		mensaje2="La maquina ha elegido tijera"

	if mano_maquina==mano_jugador:
		mensaje="Es un empate!"

	elif mano_jugador=="piedra":
		if mano_maquina=="papel":
			mensaje="La maquina gana"
		else:
			mensaje="El jugador gana"

	elif mano_jugador=="papel":
		if mano_maquina=="tijera":
			mensaje="La maquina gana"
		else:
			mensaje="El jugador gana"

	elif mano_jugador=="tijera":
		if mano_maquina=="piedra":
			mensaje="La maquina gana"
		else:
			mensaje="El jugador gana"		

	else:
		mensaje2=""
		mensaje="Por favor elija una opción antes de jugar"

	mensaje_impreso2.set(mensaje2)
	mensaje_impreso1.set(mensaje)
	mano_jugador=""
	

#---------------- Poner el mensaje en pantalla-----------------
	
pantalla1=Entry(frame, textvariable=mensaje_impreso1)
pantalla1.grid(row=4, column=0,padx=10,pady=10, columnspan=4)
pantalla1.config(bg="black", width=40, fg="#03f943")

pantalla2=Entry(frame, textvariable=mensaje_impreso2)
pantalla2.grid(row=3, column=0,padx=10,pady=10, columnspan=4)
pantalla2.config(bg="black", width=40,  fg="#03f943")


#-----------------Creación del texto para el juego-------------
texto=Label(frame, text="Elija una de las la opción que desea jugar: ")
texto.grid(row=0, column=1,padx=10, pady=10, columnspan=3)



#-----------------Creacion de Botones---------------------------
boton_piedra=Button(frame, text="Piedra", width=5, command= lambda:eleccion("piedra"))
boton_piedra.grid(row=1, column=1)
boton_papel=Button(frame, text="Papel", width=5, command= lambda:eleccion("papel"))
boton_papel.grid(row=1, column=2)
boton_tijera=Button(frame,text="Tijera",width=5, command= lambda:eleccion("tijera"))
boton_tijera.grid(row=1, column=3)
boton_jugar=Button(frame, text="Jugar", width=5, command= lambda:jugar())
boton_jugar.grid(row=5, column=2)


raiz.mainloop()