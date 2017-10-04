from tkinter import *

janela= Tk()

lb1= Label(janela, text="Label1")
lb2= Label(janela, text="Label2")

lb1.grid(row=12, column=12)
lb2.grid(row=13, column=13)


janela.geometry("500x200+600+200")

janela.mainloop()

## propriedade roll(linha) e column(coluna)