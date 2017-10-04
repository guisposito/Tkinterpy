from tkinter import *

janela= Tk()
#rowspan e columnspan mesclar linhas e colunas


lb1 = Label(janela, width=15, height=6, bg="red")
lb2 = Label(janela, width=15, height=6, bg="blue")
lb3 = Label(janela, width=15, height=6, bg="black")
lb4 = Label(janela, width=15, height=6, bg="yellow")

lb1.grid(row=0, column=0)
lb2.grid(row=0, column=0)
lb3.grid(row=0, column=0)
lb4.grid(row=0, column=0)

janela.geometry("500x10+500+200")
janela.mainloop()