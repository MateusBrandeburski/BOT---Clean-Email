from functions_robo import MeuRobo
from tkinter import Tk

windows = Tk()
robo = MeuRobo()

windows.title('Robo - Clean Email')
windows.mainloop()

def pegar_posicao_mouse():

    robo.pegar_posicao()


def bot():

    while True:
        robo.clicar(x=376, y=1277)
        robo.clicar(x=408, y=1463)
        robo.clicar(x=500, y=1276)
        robo.aguardar(1.8)
       
               
# bot()
