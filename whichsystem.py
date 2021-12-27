from tkinter import *
import os
import tkinter

ventana = Tk()
ventana.title("Which System V1.0")
ventana.geometry("500x700")


l = Label(ventana, text= "Which System")
l.config(font=("Console", 20))

l.pack()

#Entrada de texto para la direccion ip
ip = Label(ventana, text="Direccion IP: ").pack(anchor=NW)
ip_entrada = Entry(ventana)
ip_entrada.place(x=75, y=40)

#Cachar la direccion ip
def cacha():
    resultado = ip_entrada.get()
    print(resultado)
    ip_entrada.delete(0, END)
    
    response = os.system ("ping " + resultado)
    print(response)
    #Imprimir direccion ip
    
    

resultado = ip_entrada.get()


#Boton para enviar la direccion ip
ip_enviar = Button(ventana, text = "Enviar", command=cacha)
ip_enviar.place(x=200, y=35)






ventana.mainloop()