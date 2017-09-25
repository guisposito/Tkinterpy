#exemplo usando botão 
from tkinter import *

def bt_click():
	print("bt_click")

	#lb["text"] = "Funcionou!!"

def teste():
	print("deu certo")

janela= Tk()

bt = Button(janela, width=20, text="OK", command=bt_click())
bt.place(x=100, y=100)

bt1= Button(janela, width=25, text="Teste", command=teste())
bt1.place(x=200, y=150)

lb= Label(janela, text="Teste01")
lb.place(x=100, y=150)

janela.geometry("300x300+200+200")
janela.mainloop()
