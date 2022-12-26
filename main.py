from functions_robo import MeuRobo
from front_tkinter import FrontEnd


robo = MeuRobo()
front = FrontEnd()


class Main():

    def pegar_posicao_mouse(self):
        robo.pegar_posicao()


    def bot(self):
        
        while True:

            robo.clicar(front.pegar_dado_1)
            print(front.pegar_dado_1)

            robo.clicar(front.pegar_dado_2)
            robo.clicar(front.pegar_dado_3)

            robo.aguardar(1.8)

      


