from tkinter import *

janela=Tk()
#PROPRIEDADE ANCHOR
#como se fosse uma bulssula norte sul leste oeste e center
'''
lb1= Label(janela, text="side1", bg="red")
lb2= Label(janela, text="side2", bg="red")
lb3= Label(janela, text="anchor1", bg="blue")
lb4= Label(janela, text="anchor2", bg="blue")

lb1.pack(side=LEFT)
lb2.pack(side=LEFT)
lb3.pack(anchor=W)
lb4.pack(anchor=W)
# N S E W NW NE SE SW
'''
lb1= Label(janela, text="ANCHORNORTE", bg="red")
lb2= Label(janela, text="ANCHORSUL", bg="red")
lb3= Label(janela, text="ANCHORLESTE", bg="blue")
lb4= Label(janela, text="ANCHOROESTE", bg="blue")
lb5= Label(janela, text="ANCHORNW", bg="red")
lb6= Label(janela, text="ANCHORNE", bg="red")
lb7= Label(janela, text="ANCHORSW", bg="blue")
lb8= Label(janela, text="ANCHOROSE", bg="blue")
lb9= Label(janela, text="ANCHOROCENTER", bg="pink")

lb1.pack(anchor=N)
lb2.pack(anchor=S)
lb3.pack(anchor=E)
lb4.pack(anchor=W)
lb5.pack(anchor=NW)
lb6.pack(anchor=NE)
lb7.pack(anchor=SW)
lb8.pack(anchor=SE)
lb9.pack(anchor=CENTER)

janela["bg"]= "black"
janela.geometry("400x300+200+200")
janela.mainloop()