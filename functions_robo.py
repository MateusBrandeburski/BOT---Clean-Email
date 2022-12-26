import pyautogui
import pyperclip
from time import sleep



class MeuRobo():

    def __init__(self):
        pyautogui.PAUSE = 1

    def abrir_navegador(self):
        pyautogui.press("win")
        pyautogui.click(x=531, y=464)

    def escolher_site(self, texto):
        pyautogui.click(x=420,y=77)
        self.escrever_e_enter(texto)

    def aguardar(self,tempo):
        sleep(tempo)

    def escrever_e_enter(self, texto):
        pyautogui.write(texto)
        pyautogui.press("enter")

    def pesquisar_no_campo(self, texto):
        pyautogui.click(x=1336, y=532)
        self.escrever_e_enter(texto)

    def clicar_imagem(self):
        pyautogui.click(x=749, y=699)

    
    def clicar(self, x, y, botao="left"): #botao por padrão ele é left
        
        pyautogui.click(x=x,y=y, button=botao)
    


    def pegar_posicao(self):
        # dá 5 segundos para pessoa posicionar o mouse
        for i in range(0,5,1):
            print(f"pegando posicao em {5 - i} segundos")
            sleep(1)

        # método que pega a posição do mouse
        posicao = pyautogui.position()
        print(posicao)       


    

    
        

        
    
