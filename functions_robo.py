import pyautogui
import pyperclip
from time import sleep
import keyboard

class MeuRobo():

    def __init__(self): # vai passar esse tempo na instância da classe
        
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

    def extrair_link(self):
        pyautogui.click(x=497, y=692, button="right") # button = esquerda do mouse
        pyautogui.press("up")
        pyautogui.press("up")
        pyautogui.press("up")
        pyautogui.press("enter")
        texto = pyperclip.paste()
        print(texto)

    
    def clicar(self, x, y, botao="left"): #por padrão ele é left
        pyautogui.click(x=x,y=y, button=botao)
    
    def pegar_posicao(self):

        for i in range(0,5,1):

            print(f"pegando posicao em {5 - i} segundos")
            sleep(1)
        
        print(pyautogui.position())       

    def capturar_teclas(self):
          keyboard.wait('a')
        
    
