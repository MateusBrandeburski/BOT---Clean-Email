import pyautogui
from time import sleep
import tkinter as tk


windows = tk.Tk()


        # título na barra da janela
windows.title('Robo - Clean Email')


def mouse():
    for i in range(0,5,1):
        print(f"pegando posicao em {5 - i} segundos")
        sleep(1)

# método que pega a posição do mouse
posicao = pyautogui.position()
print(posicao)    


        # botão que clica
text1 = tk.Label(text='Encontre a posição do seu mouse', fg='white', bg='green', width=50, height=10)
text1.grid(row=0, column=0)
botao = tk.Button(text='Posição do Mouse', command=mouse)
botao.grid(row=0, column=2)




## mensagem com as coordanadas aparece na tela.
text1 = tk.Label(text='{}'.format (mouse))
text1.grid(row=1, column=0, columnspan=2)

# primeiro clique do bot
text2 = tk.Label(text='Primeiro Click')
text2.grid(row=2, column=0)
caixa2_input = tk.Entry()
caixa2_input.grid(row=2, column=1)

# pegar informaão da caixa imput1

windows.mainloop()