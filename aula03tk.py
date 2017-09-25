import tkinter

janela= tkinter.Tk()
janela.title("Janela Principal")

janela["bg"]= "green"
janela["background"] = "green"

# Largura x Altura +Esqueda do video+Topo do video
#300x300+100+100
janela.geometry("800x300+100+100")

janela.mainloop()
