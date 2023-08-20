from tkinter import *
import random

raiz=Tk()

frame=Frame(raiz, height=300, width=300)
frame.pack()

imagen=PhotoImage(file="circulo.png")


ocupado1=False
ocupado2=False
ocupado3=False
ocupado4=False
ocupado5=False
ocupado6=False
ocupado7=False
ocupado8=False
ocupado9=False
repetir=""
listao=[]
listax=[]
win=False
winx=False
mensaje_impreso1=StringVar()



#--------------Tablero---------------------------
boton1=Button(frame, height=10, width=10, command= lambda :cambio(1))
boton2=Button(frame, height=10, width=10, command= lambda:cambio(2))
boton3=Button(frame, height=10, width=10, command= lambda:cambio(3))
boton4=Button(frame, height=10, width=10,  command= lambda:cambio(4))
boton5=Button(frame, height=10, width=10, command= lambda:cambio(5))
boton6=Button(frame, height=10, width=10, command= lambda:cambio(6))
boton7=Button(frame, height=10, width=10, command= lambda:cambio(7))
boton8=Button(frame, height=10, width=10, command= lambda:cambio(8))
boton9=Button(frame, height=10, width=10, command= lambda:cambio(9))

boton1.grid(row=1, column=1)
boton2.grid(row=1, column=2)
boton3.grid(row=1, column=3)
boton4.grid(row=2, column=1)
boton5.grid(row=2, column=2)
boton6.grid(row=2, column=3)
boton7.grid(row=3, column=1)
boton8.grid(row=3, column=2)
boton9.grid(row=3, column=3)

#-------------------Pantalla-------------------------------

pantalla1=Entry(frame, textvariable=mensaje_impreso1)
pantalla1.grid(row=0, column=1,padx=10,pady=10, columnspan=3)
pantalla1.config(bg="black", width=40, fg="#03f943")



#------------------Tricky--------------------------------


def generadoro(lista):
	global listao
	global listax
	global win
	localwin=True
	for i in lista:
		if i in listao:
			a=0# algo tenía que poner :V
		else:
			localwin=False
	if localwin==True:
		win=True

def generadorx(lista):
	global listao
	global listax
	global winx
	localwinx=True
	for i in lista:
		if i in listax:
			a=0# algo tenía que poner :V
		else:
			localwinx=False
	if localwinx==True:
		winx=True




def lineao():
	global win
	generadoro([1,2,3])
	if win==True:
		mensaje_impreso1.set("Triky, el jugador ha ganado")
	generadoro([4,5,6])
	if win==True:
		mensaje_impreso1.set("Triky, el jugador ha ganado")
	generadoro([7,8,9])
	if win==True:
		mensaje_impreso1.set("Triky, el jugador ha ganado")
	generadoro([1,4,7])
	if win==True:
		mensaje_impreso1.set("Triky, el jugador ha ganado")
	generadoro([2,5,8])
	if win==True:
		mensaje_impreso1.set("Triky, el jugador ha ganado")
	generadoro([3,6,9])
	if win==True:
		mensaje_impreso1.set("Triky, el jugador ha ganado")
	generadoro([1,5,9])
	if win==True:
		mensaje_impreso1.set("Triky, el jugador ha ganado")
	generadoro([3,5,7])
	if win==True:
		mensaje_impreso1.set("Triky, el jugador ha ganado")


def lineax():
	global winx
	generadorx([1,2,3])
	if winx==True:
		mensaje_impreso1.set("Triky, la maquina ha ganado")
	generadorx([4,5,6])
	if winx==True:
		mensaje_impreso1.set("Triky, la maquina ha ganado")
	generadorx([7,8,9])
	if winx==True:
		mensaje_impreso1.set("Triky, la maquina ha ganado")
	generadorx([1,4,7])
	if winx==True:
		mensaje_impreso1.set("Triky, la maquina ha ganado")
	generadorx([2,5,8])
	if winx==True:
		mensaje_impreso1.set("Triky, la maquina ha ganado")
	generadorx([3,6,9])
	if winx==True:
		mensaje_impreso1.set("Triky, la maquina ha ganado")
	generadorx([1,5,9])
	if winx==True:
		mensaje_impreso1.set("Triky, la maquina ha ganado")
	generadorx([3,5,7])
	if winx==True:
		mensaje_impreso1.set("Triky, la maquina ha ganado")









#------------------selección de la maquina-------------------------

def maquina():
	global ocupado1
	global ocupado2
	global ocupado3
	global ocupado4
	global ocupado5
	global ocupado6
	global ocupado7
	global ocupado8
	global ocupado9
	global repetir

	h=random.randint(1,9)

	if h==1:
		repetir=ocupado1
	elif h==2:
		repetir=ocupado2
	elif h==3:
		repetir=ocupado3
	elif h==4:
		repetir=ocupado4
	elif h==5:
		repetir=ocupado5
	elif h==6:
		repetir=ocupado6
	elif h==7:
		repetir=ocupado7
	elif h==8:
		repetir=ocupado8
	elif h==9:
		repetir=ocupado9

	while repetir==True: 
		h=random.randint(1,9)
		if h==1:
			repetir=ocupado1
		elif h==2:
			repetir=ocupado2
		elif h==3:
			repetir=ocupado3
		elif h==4:
			repetir=ocupado4
		elif h==5:
			repetir=ocupado5
		elif h==6:
			repetir=ocupado6
		elif h==7:
			repetir=ocupado7
		elif h==8:
			repetir=ocupado8
		elif h==9:
			repetir=ocupado9

	
	if h==1:
		boton1=Button(frame, text="X", height=10, width=10)
		boton1.grid(row=1, column=1)
		ocupado1=True
		listax.append(h)

	elif h==2:
		boton2=Button(frame, text="X", height=10, width=10)
		boton2.grid(row=1, column=2)
		ocupado2=True
		listax.append(h)

	elif h==3:
		boton3=Button(frame, text="X", height=10, width=10)
		boton3.grid(row=1, column=3)
		ocupado3=True
		listax.append(h)

	elif h==4:
		boton4=Button(frame, text="X", height=10, width=10)
		boton4.grid(row=2, column=1)
		ocupado4=True
		listax.append(h)

	elif h==5:
		boton5=Button(frame, text="X", height=10, width=10)
		boton5.grid(row=2, column=2)
		ocupado5=True
		listax.append(h)

	elif h==6:
		boton6=Button(frame, text="X", height=10, width=10)
		boton6.grid(row=2, column=3)
		ocupado6=True
		listax.append(h)

	elif h==7:
		boton7=Button(frame, text="X", height=10, width=10)
		boton7.grid(row=3, column=1)
		ocupado7=True
		listax.append(h)

	elif h==8:
		boton8=Button(frame, text="X", height=10, width=10)
		boton8.grid(row=3, column=2)
		ocupado8=True
		listax.append(h)

	elif h==9:
		boton9=Button(frame, text="X", height=10, width=10)
		boton9.grid(row=3, column=3)
		ocupado9=True
		listax.append(h)

#----------------------Función de cambio de boton------------------

def cambio(num):
	global ocupado1
	global ocupado2
	global ocupado3
	global ocupado4
	global ocupado5
	global ocupado6
	global ocupado7
	global ocupado8
	global ocupado9
	global listao
	if num==1:
		boton1=Button(frame, text="O", height=10, width=10)
		boton1.grid(row=1, column=1)
		ocupado1=True
		listao.append(num)

	elif num==2:
		boton2=Button(frame, text="O", height=10, width=10)
		boton2.grid(row=1, column=2)
		ocupado2=True
		listao.append(num)

	elif num==3:
		boton3=Button(frame, text="O", height=10, width=10)
		boton3.grid(row=1, column=3)
		ocupado3=True
		listao.append(num)

	elif num==4:
		boton4=Button(frame, text="O", height=10, width=10)
		boton4.grid(row=2, column=1)
		ocupado4=True
		listao.append(num)

	elif num==5:
		boton5=Button(frame, text="O", height=10, width=10)
		boton5.grid(row=2, column=2)
		ocupado5=True
		listao.append(num)

	elif num==6:
		boton6=Button(frame, text="O", height=10, width=10)
		boton6.grid(row=2, column=3)
		ocupado6=True
		listao.append(num)

	elif num==7:
		boton7=Button(frame, text="O", height=10, width=10)
		boton7.grid(row=3, column=1)
		ocupado7=True
		listao.append(num)

	elif num==8:
		boton8=Button(frame, text="O", height=10, width=10)
		boton8.grid(row=3, column=2)
		ocupado8=True
		listao.append(num)

	elif num==9:
		boton9=Button(frame, text="O", height=10, width=10)
		boton9.grid(row=3, column=3)
		ocupado9=True
		listao.append(num)	

	final=False
	if ocupado1==True and ocupado2==True and ocupado3==True and ocupado4==True and ocupado5==True and ocupado6==True and ocupado7==True and ocupado8==True and ocupado9==True:
		final=True
	if final==False:
		maquina()

	lineao()
	lineax()


raiz.mainloop()