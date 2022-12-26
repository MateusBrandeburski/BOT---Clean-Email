import tkinter as tk
from functions_robo import MeuRobo



robo = MeuRobo()

class FrontEnd(): 


    def frontend(self):

        # instâncias dos objetos
        windows = tk.Tk()

        # título na barra da janela
        windows.title('Robo - Clean Email')

        # botão que clica
        text1 = tk.Label(text='Encontre a posição do seu mouse', fg='white', bg='green', width=50, height=10)
        text1.grid(row=0, column=0)
        botao = tk.Button(text='Posição do Mouse', command=robo.pegar_posicao)
        botao.grid(row=0, column=1)
        ## mensagem com as coordanadas aparece na tela.
        # text1 = tk.Label(text='{}'.format (robo.pegar_posicao))
        # text1.grid(row=4, column=0, columnspan=2)

        # primeiro clique do bot
        text2 = tk.Label(text='Primeiro Click')
        text2.grid(row=1, column=0)

        global caixa2_input
        caixa2_input = tk.Entry()
        caixa2_input.grid(row=1, column=1)

        botao = tk.Button(text='Enviar Posição do Mouse 1', command=front_tk.pegar_dado_1)
        botao.grid(row=1, column=2)

        # segundo click do bot
        text3 = tk.Label(text='Segundo Click')
        text3.grid(row=2, column=0)

        global caixa3_input
        caixa3_input = tk.Entry()
        caixa3_input.grid(row=2, column=1)

        botao2 = tk.Button(text='Enviar Posição do Mouse 2', command=front_tk.pegar_dado_2)
        botao2.grid(row=2, column=2)
        

        # terceiro click do bot
        text4 = tk.Label(text='Terceiro Click')
        text4.grid(row=3, column=0)

        global caixa4_input
        caixa4_input = tk.Entry()
        caixa4_input.grid(row=3, column=1)

        botao3 = tk.Button(text='Enviar posisção do Mouse 3', command=front_tk.pegar_dado_3)
        botao3.grid(row=3, column=2)

        # iniciar bot
        botao4 = tk.Button(text='Inicar Robo - Clean Email', command=Main.bot)
        botao4.grid(row=4, columnspan=3)

        windows.mainloop()


    def pegar_dado_1(self):
        posicao1 = caixa2_input.get()
        global x1
        x1 = int(posicao1[2:5])
        print(x1)
        global y1
        y1 = int(posicao1[9:14])
        print(y1)

    def pegar_dado_2(self):
        posicao2 = caixa3_input.get()
        global x2
        x2 = int(posicao2[2:5])
        global y2
        y2 = int(posicao2[9:14])

    def pegar_dado_3(self):
        posicao3 = caixa4_input.get()
        global x3
        x3 = int(posicao3[2:5])
        global y3
        y3 = int(posicao3[9:14])


class Main():
    
    def bot():
   
        while True:
            robo.clicar(x=x1,y=y1)
            robo.clicar(x=x2, y=y2)
            robo.clicar(x=x3, y=y3)
            robo.aguardar(1.8)
      

front_tk = FrontEnd()
front_tk.frontend()