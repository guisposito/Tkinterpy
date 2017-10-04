from tkinter import *

janela= Tk()


#stick= sentido oque o componente deve ter

lb1= Label(janela, text="ESPACO", width="15", height=3, bg="blue")
lbhorizontal=Label(janela, text="horizontal", bg="yellow")
lbvertical= Label(janela, text="vertical", bg="yellow")

lb1.grid(row=0, column=0)
lbhorizontal.grid(row=1, column=0, sticky=E)
lbvertical.grid(row=0, column=1, sticky=N)

janela.geometry("200x100+100+100")
janela.mainloop()