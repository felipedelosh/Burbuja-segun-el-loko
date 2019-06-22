"""
FelipedelosH

6/20/2019

Se desea hacer un programa que dados 320 numeros aleatoreos de 0 a 400
los organice por medio de burbuja y muestre paso a paso con un slider que retarde
"""

from tkinter import *
from random import randint
from threading import *
from time import sleep

class GraphiBubbleShort():
    def __init__(self):
        self.pantalla = Tk()
        self.telaControl = Canvas(self.pantalla,width=640, height=80 ,bg="snow")
        self.telaGraficas = Canvas(self.pantalla,width=640, height=400 ,bg="white")
        self.btnPlay = Button(self.telaControl, text="PLAY", command=self.play)
        self.btnPausa = Button(self.telaControl, text="PAUSE", command=self.pause)
        self.lblIteracion = Label(self.telaControl, text="Iteracion: 0")

        """Variables"""
        self.vectorNumeros = [] # aqui se guardan los 640 numeros
        self.estoyRondando = False  # controla si el programa esta en ejecucion
        self.intSlider = 0.5

        self.hilo = Thread(target=self.run)
        """Preparativos para lanzar el programa"""
        # Se inicia el hilo
        self.hilo.start()
        # Se rellena el vector
        self.rellemarVectorNum()
        """Se muestra todo"""
        self.visualizarInterfaz()

    def visualizarInterfaz(self):
        self.pantalla.title("Burbuja by loko")
        self.pantalla.geometry("640x480")

        self.telaControl.place(x=0, y=0)
        self.btnPlay.place(x=10, y=20)
        self.btnPausa.place(x=60, y=20)
        self.lblIteracion.place(x=10, y=50)
        self.telaGraficas.place(x=0, y=80)

        """Se procede a graficar el vector"""
        self.graficarVector()
        self.pantalla.mainloop()

    def rellemarVectorNum(self):
        if not self.estoyRondando:
            self.vectorNumeros.clear()
            for i in range(320):
                self.vectorNumeros.append(randint(1, 400))

    def graficarVector(self):
        for i in range(0, len(self.vectorNumeros)):
            x0 = 1 + (2*i)
            self.telaGraficas.create_rectangle(x0, 0, x0+1, self.vectorNumeros[i], tags="vector")

    def play(self):
        self.pantalla.title("Burbuja by loko:PLAY")
        self.estoyRondando = True

    def pause(self):
        self.pantalla.title("Burbuja by loko:PAUSE")
        self.estoyRondando = False

    def run(self):
        contadori = 0
        contadorj = 0
        aux = 0
        Iteracion = 0
        while True:
            while self.estoyRondando and contadori < len(self.vectorNumeros):
                # procedo a instaciar j en lo que no esta ordenado
                contadorj = 0
                # procedo a borrar los numeros
                self.telaGraficas.delete("vector")
                while self.estoyRondando and contadorj < len(self.vectorNumeros)-(contadori+1):
                    if self.vectorNumeros[contadorj] < self.vectorNumeros[contadorj+1]:
                        aux = self.vectorNumeros[contadorj+1]
                        self.vectorNumeros[contadorj+1] = self.vectorNumeros[contadorj]
                        self.vectorNumeros[contadorj] = aux
                    
                    if self.estoyRondando:
                        Iteracion = Iteracion + 1
                        self.lblIteracion['text'] = "Iteracion: "+str(Iteracion)
                        contadorj = contadorj + 1
                
                # se grafica el vector
                self.graficarVector()
                self.telaGraficas.update_idletasks()
                
                sleep(0.1)
                """Se incrementa i"""
                if self.estoyRondando:
                    contadori = contadori + 1



sw = GraphiBubbleShort()