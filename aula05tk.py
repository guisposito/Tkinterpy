#GERENCIADORES DE LEIAUTE
#UM gerenciador de leiaute define a organização dentro de um container
# a biblioteca do tkinter disponibilzia 3 tipos de gerenciadores
# o place, os widgets sao dispostos conforme suas coordenadas x e y
# pack empacota os widgets na horizontal ou vertical 
# grid os wwidgets sao inseridos num sistema de celulas definidas
## PLACE

from tkinter import *

janela = Tk()

lb = Label(janela, text="Programa 01!")
lb.place(x= 100, y=100)
# w x h + l + t
janela.geometry("300x300+200+200")

janela.mainloop()