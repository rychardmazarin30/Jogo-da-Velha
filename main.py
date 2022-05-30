from tkinter import *
from tkinter import ttk

white = '#FFFFFF'
darkBlack = '#333333'
orange = '#fcc058'
value = '#38576b'
blue = '#2c59de'
yellow = '#fff873'
green = '#1ba611'
red = '#c41212'
know = "#fcfbf7"
black = '#3b3b3b' 

j = Tk()
j.title("TIC-TAC-TOE")
j.geometry('260x370')
j.configure(bg=darkBlack)

frame_cima = Frame(j, width=240, height=100, bg=black, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(j, width=240, height=250, bg=darkBlack, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)

# Configurando Tudo 

app_x = Label(
    frame_cima, 
    text='X', 
    height=1, 
    relief='flat',
    anchor='center',
    font=('Ivy 40 bold'),
    bg=black,
    fg=red)
app_x.place(x=25, y=10)

app_j1 = Label(
    frame_cima,
    text='Player One',
    height=1,
    relief='flat',
    anchor='center',
    font=('Ivy 8 bold'),
    bg=black,
    fg=white)
app_j1.place(x=16, y=65)

app_x_pontos = Label(
    frame_cima,
    text='0',
    height=1,
    relief='flat',
    anchor='center',
    font=('Ivy 30 bold'),
    bg=black,
    fg=white)
app_x_pontos.place(x=80, y=20)

app_separador = Label(
    frame_cima,
    text=':',
    height=1,
    relief='flat',
    anchor='center',
    font=('Ivy 30 bold'),
    bg=black,
    fg=white)
app_separador.place(x=109, y=20)

app_o = Label(
    frame_cima,
    text='O',
    height=1,
    relief='flat',
    anchor='center',
    font=('Ivy 40 bold'),
    bg=black,
    fg=green)
app_o.place(x=170, y=10)

app_j2 = Label(
    frame_cima,
    text='Player Two',
    height=1,
    relief='flat',
    anchor='center',
    font=('Ivy 8 bold'),
    bg=black,
    fg=white)
app_j2.place(x=163, y=65)

app_o_pontos = Label(
    frame_cima,
    text='0',
    height=1,
    relief='flat',
    anchor='center',
    font=('Ivy 30 bold'),
    bg=black,
    fg=white)
app_o_pontos.place(x=130, y=20)

# Criando Funções

jogador_1 = "X"
jogador_2 = "O"

pontos_X = 0
pontos_O = 0

table = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']
]

jogando = 'X'
jogar = ''
contador = 0
contador_rodadas = 0

def start_game():
    # Para controle do jogo
    def controlar(i):
        global jogando  
        global contador  
        global jogar

        #Comparando o valor recebido
        if i == str(1):
            # Verificando se aquela posição está vazia
            if b_1['text'] == '':
                # Verificando quem esta jogando e assim definir a cor do símbolo
                if jogando == "X":
                    cor = white
                    b_1['bg'] = red
                if jogando == "O":
                    cor = white
                    b_1['bg'] = green

                # Definindo a cor do texto do botão e marcar aquela posição da tabela com o valor do jogador atual

                b_1['fg'] = cor
                b_1['text'] = jogando
                table[0][0] = jogando

                # Verificando quem está jogando para poder trocar de jogador
                if jogando == "X":
                    jogando = 'O'
                    joga = 'Player One'
                else:
                    jogando = 'X'
                    joga = 'Player Two'

                # Incrementar o contador para a proxima jogada
                contador += 1
                    
        if i == str(2):
            # Verificando se aquela posição está vazia
            if b_2['text'] == '':
                # Verificando quem esta jogando e assim definir a cor do símbolo
                if jogando == "X":
                    cor = white
                    b_2['bg'] = red
                if jogando == "O":
                    cor = white
                    b_2['bg'] = green

                # Definindo a cor do texto do botão e marcar aquela posição da tabela com o valor do jogador atual

                b_2['fg'] = cor
                b_2['text'] = jogando
                table[0][1] = jogando

                # Verificando quem está jogando para poder trocar de jogador
                if jogando == "X":
                    jogando = 'O'
                    joga = 'Player One'
                else:
                    jogando = 'X'
                    joga = 'Player Two'

                # Incrementar o contador para a proxima jogada
                contador += 1
            
        if i == str(3):
            # Verificando se aquela posição está vazia
            if b_3['text'] == '':
                # Verificando quem esta jogando e assim definir a cor do símbolo
                if jogando == "X":
                    cor = white
                    b_3['bg'] = red
                if jogando == "O":
                    cor = white
                    b_3['bg'] = green

                # Definindo a cor do texto do botão e marcar aquela posição da tabela com o valor do jogador atual

                b_3['fg'] = cor
                b_3['text'] = jogando
                table[0][2] = jogando

                # Verificando quem está jogando para poder trocar de jogador
                if jogando == "X":
                    jogando = 'O'
                    joga = 'Player One'
                else:
                    jogando = 'X'
                    joga = 'Player Two'

                # Incrementar o contador para a proxima jogada
                contador += 1

        if i == str(4):
            # Verificando se aquela posição está vazia
            if b_4['text'] == '':
                # Verificando quem esta jogando e assim definir a cor do símbolo
                if jogando == "X":
                    cor = white
                    b_4['bg'] = red
                if jogando == "O":
                    cor = white
                    b_4['bg'] = green

                # Definindo a cor do texto do botão e marcar aquela posição da tabela com o valor do jogador atual

                b_4['fg'] = cor
                b_4['text'] = jogando
                table[1][0] = jogando

                # Verificando quem está jogando para poder trocar de jogador
                if jogando == "X":
                    jogando = 'O'
                    joga = 'Player One'
                else:
                    jogando = 'X'
                    joga = 'Player Two'

                # Incrementar o contador para a proxima jogada
                contador += 1

        if i == str(5):
            # Verificando se aquela posição está vazia
            if b_5['text'] == '':
                # Verificando quem esta jogando e assim definir a cor do símbolo
                if jogando == "X":
                    cor = white
                    b_5['bg'] = red
                if jogando == "O":
                    cor = white
                    b_5['bg'] = green

                # Definindo a cor do texto do botão e marcar aquela posição da tabela com o valor do jogador atual

                b_5['fg'] = cor
                b_5['text'] = jogando
                table[1][1] = jogando

                # Verificando quem está jogando para poder trocar de jogador
                if jogando == "X":
                    jogando = 'O'
                    joga = 'Player One'
                else:
                    jogando = 'X'
                    joga = 'Player Two'

                # Incrementar o contador para a proxima jogada
                contador += 1

        if i == str(6):
            # Verificando se aquela posição está vazia
            if b_6['text'] == '':
                # Verificando quem esta jogando e assim definir a cor do símbolo
                if jogando == "X":
                    cor = white
                    b_6['bg'] = red
                if jogando == "O":
                    cor = white
                    b_6['bg'] = green

                # Definindo a cor do texto do botão e marcar aquela posição da tabela com o valor do jogador atual

                b_6['fg'] = cor
                b_6['text'] = jogando
                table[1][2] = jogando

                # Verificando quem está jogando para poder trocar de jogador
                if jogando == "X":
                    jogando = 'O'
                    joga = 'Player One'
                else:
                    jogando = 'X'
                    joga = 'Player Two'

                # Incrementar o contador para a proxima jogada
                contador += 1
   
        if i == str(7):
            # Verificando se aquela posição está vazia
            if b_7['text'] == '':
                # Verificando quem esta jogando e assim definir a cor do símbolo
                if jogando == "X":
                    cor = white
                    b_7['bg'] = red
                if jogando == "O":
                    cor = white
                    b_7['bg'] = green

                # Definindo a cor do texto do botão e marcar aquela posição da tabela com o valor do jogador atual

                b_7['fg'] = cor
                b_7['text'] = jogando
                table[2][0] = jogando

                # Verificando quem está jogando para poder trocar de jogador
                if jogando == "X":
                    jogando = 'O'
                    joga = 'Player One'
                else:
                    jogando = 'X'
                    joga = 'Player Two'

                # Incrementar o contador para a proxima jogada
                contador += 1
   
        if i == str(8):
            # Verificando se aquela posição está vazia
            if b_8['text'] == '':
                # Verificando quem esta jogando e assim definir a cor do símbolo
                if jogando == "X":
                    cor = white
                    b_8['bg'] = red
                if jogando == "O":
                    cor = white
                    b_8['bg'] = green

                # Definindo a cor do texto do botão e marcar aquela posição da tabela com o valor do jogador atual

                b_8['fg'] = cor
                b_8['text'] = jogando
                table[2][1] = jogando

                # Verificando quem está jogando para poder trocar de jogador
                if jogando == "X":
                    jogando = 'O'
                    joga = 'Player One'
                else:
                    jogando = 'X'
                    joga = 'Player Two'

                # Incrementar o contador para a proxima jogada
                contador += 1
   
        if i == str(9):
            # Verificando se aquela posição está vazia
            if b_9['text'] == '':
                # Verificando quem esta jogando e assim definir a cor do símbolo
                if jogando == "X":
                    cor = white
                    b_9['bg'] = red
                if jogando == "O":
                    cor = white
                    b_9['bg'] = green

                # Definindo a cor do texto do botão e marcar aquela posição da tabela com o valor do jogador atual

                b_9['fg'] = cor
                b_9['text'] = jogando
                table[2][2] = jogando

                # Verificando quem está jogando para poder trocar de jogador
                if jogando == "X":
                    jogando = 'O'
                    joga = 'Player One'
                else:
                    jogando = 'X'
                    joga = 'Player Two'

                # Incrementar o contador para a proxima jogada
                contador += 1

        # Após o contador ser maior ou igual a 5, verifica se houve algum vencedor de acordo com os padrões seguintes
        if contador >= 5:

            # Linhas
            if table[0][0] == table[0][1] == table[0][2]!="":
                winner(jogando)
            elif table[1][0] == table[1][1] == table[1][2]!="":
                winner(jogando)
            elif table[2][0] == table[2][1] == table[2][2]!="":
                winner(jogando)

            # Colunas
            if table[0][0] == table[1][0] == table[2][0]!="":
                winner(jogando)
            elif table[0][1] == table[1][1] == table[2][1]!="":
                winner(jogando)
            elif table[0][2] == table[1][2] == table[2][2]!="":
                winner(jogando)

            # Diagonais
            if table[0][0] == table[1][1] == table[2][2]!="":
                winner(jogando)
            elif table[0][2] == table[1][1] == table[2][0]!="":
                winner(jogando)

            # Empate
            if contador >= 9:
                winner('Deu Velha!')

    # Decidir o vencedor
    def winner(i):
        global table
        global jogando
        global pontos_X 
        global pontos_O
        global contador_rodadas
        global contador

        # Limpando os botões
        b_1['text'] = ''
        b_2['text'] = ''
        b_3['text'] = ''
        b_4['text'] = ''
        b_5['text'] = ''
        b_6['text'] = ''
        b_7['text'] = ''
        b_8['text'] = ''
        b_9['text'] = ''

        # Limpando o Backgound
        b_1['bg'] = darkBlack
        b_2['bg'] = darkBlack
        b_3['bg'] = darkBlack
        b_4['bg'] = darkBlack
        b_5['bg'] = darkBlack
        b_6['bg'] = darkBlack
        b_7['bg'] = darkBlack
        b_8['bg'] = darkBlack
        b_9['bg'] = darkBlack


        # Bloqueando os botões
        b_1['state'] = 'disable'
        b_2['state'] = 'disable'
        b_3['state'] = 'disable'
        b_4['state'] = 'disable'
        b_5['state'] = 'disable'
        b_6['state'] = 'disable'
        b_7['state'] = 'disable'
        b_8['state'] = 'disable'
        b_9['state'] = 'disable'

        table = [
            ['1','2','3'],
            ['4','5','6'],
            ['7','8','9']
                ]

        app_vencedor = Label(
        frame_baixo,
            text='',
            width=17,
            relief='flat',
            anchor='center',
            font=('Ivy 13 bold'),
            bg=darkBlack,
            fg=orange)
        app_vencedor.place(x=40, y=93)

        if i == "X":
            pontos_O += 1
            app_vencedor['text'] = "Player Two Win!"
            app_o_pontos['text'] = pontos_O
        
        if i == "O":
            pontos_X += 1
            app_vencedor['text'] = "Player One Win!"
            app_x_pontos['text'] = pontos_X

        if i == 'Deu Velha!':
            app_vencedor['text'] = "Velha!"

        def start():
            # Limpando os botões
            b_1['text'] = ''
            b_2['text'] = ''
            b_3['text'] = ''
            b_4['text'] = ''
            b_5['text'] = ''
            b_6['text'] = ''
            b_7['text'] = ''
            b_8['text'] = ''
            b_9['text'] = ''

            b_1['state'] = 'normal'
            b_2['state'] = 'normal'
            b_3['state'] = 'normal'
            b_4['state'] = 'normal'
            b_5['state'] = 'normal'
            b_6['state'] = 'normal'
            b_7['state'] = 'normal'
            b_8['state'] = 'normal'
            b_9['state'] = 'normal'

            # Reiniciando a tabela
            table = [
            ['1','2','3'],
            ['4','5','6'],
            ['7','8','9']
                ]

            app_vencedor.destroy()
            play.destroy()

        play = Button(
        frame_baixo,
        command=start, 
        text='PLAY AGAIN', 
        width=10,
        height=1, 
        relief='raised',
        font=('Ivy 10 bold'),
        overrelief=RIDGE,
        bg=blue,
        fg=white)
        play.place(x=82, y=215)


        def game_over():
            play.destroy()
            app_vencedor.destroy()

            end_game()

        if contador_rodadas == 4:
            game_over()
        else:
            contador_rodadas += 1
            # Reiniciando a tabela
            table = [
            ['1','2','3'],
            ['4','5','6'],
            ['7','8','9']
                ]
            contador = 0

    # Para terminar o jogo
    def end_game():
        global table
        global contador_rodadas
        global pontos_X
        global pontos_O
        global contador

        table = [
                    ['1','2','3'],
                    ['4','5','6'],
                    ['7','8','9']
                ]
        contador_rodadas = 0
        contador = 0
        pontos_X = 0
        pontos_O = 0

        # Bloqueando os botões
        b_1['state'] = 'disable'
        b_2['state'] = 'disable'
        b_3['state'] = 'disable'
        b_4['state'] = 'disable'
        b_5['state'] = 'disable'
        b_6['state'] = 'disable'
        b_7['state'] = 'disable'
        b_8['state'] = 'disable'
        b_9['state'] = 'disable'

        app_fim = Label(
        frame_baixo,
            text='Game Over',
            width=17,
            relief='flat',
            anchor='center',
            font=('Ivy 13 bold'),
            bg=darkBlack,
            fg=orange)
        app_fim.place(x=40, y=93)

        # Jogar de novo
        def play_again():
            app_x_pontos['text'] = '0'
            app_o_pontos['text'] = '0'
            app_fim.destroy()
            play.destroy()

            # Chamando a função Iniciar o jogo
            start_game()
            
        # Botão jogar de novo
        play = Button(
        frame_baixo,
        command=play_again, 
        text='PLAY', 
        width=10,
        height=1, 
        relief='raised',
        font=('Ivy 10 bold'),
        overrelief=RIDGE,
        bg=blue,
        fg=white)
        play.place(x=82, y=215)

    # Linhas Verticais

    app_l1 = Label(
        frame_baixo, 
        text='', 
        height=23, 
        relief='flat',
        pady=5,
        anchor='center',
        font=('Ivy 5 bold'),
        bg=white)
    app_l1.place(x=90, y=15)

    app_l2 = Label(
        frame_baixo, 
        text='', 
        height=23, 
        relief='flat',
        pady=5,
        anchor='center',
        font=('Ivy 5 bold'),
        bg=white)
    app_l2.place(x=157, y=15)

    # Linhas Horizontais

    app_l3 = Label(
        frame_baixo, 
        text='   ', 
        width=46, 
        relief='flat',
        padx=2,
        pady=1,
        anchor='center',
        font=('Ivy 5 bold'),
        bg=white,)
    app_l3.place(x=30, y=63)

    app_l4 = Label(
        frame_baixo, 
        text='', 
        width=46, 
        relief='flat',
        padx=2,
        pady=1,
        anchor='center',
        font=('Ivy 5 bold'),
        bg=white,)
    app_l4.place(x=30, y=127)


    # Botões

    b_1 = Button(
        frame_baixo,
        command = lambda: controlar('1'), 
        text='', 
        width=3, 
        relief='flat',
        font=('Ivy 20 bold'),
        overrelief=RIDGE,
        bg=darkBlack,)
    b_1.place(x=30, y=15)

    b_2 = Button(
        frame_baixo,
        command = lambda: controlar('2'), 
        text='', 
        width=3, 
        relief='flat',
        font=('Ivy 20 bold'),
        overrelief=RIDGE,
        bg=darkBlack,)
    b_2.place(x=96, y=15)

    b_3 = Button(
        frame_baixo,
        command = lambda: controlar('3'), 
        text='', 
        width=3, 
        relief='flat',
        font=('Ivy 20 bold'),
        overrelief=RIDGE,
        bg=darkBlack,)
    b_3.place(x=162, y=15)

    b_4 = Button(
        frame_baixo,
        command = lambda: controlar('4'), 
        text='', 
        width=3, 
        relief='flat',
        font=('Ivy 20 bold'),
        overrelief=RIDGE,
        bg=darkBlack,)
    b_4.place(x=30, y=76)

    b_5 = Button(
        frame_baixo,
        command = lambda: controlar('5'), 
        text='', 
        width=3, 
        relief='flat',
        font=('Ivy 20 bold'),
        overrelief=RIDGE,
        bg=darkBlack,)
    b_5.place(x=96, y=76)

    b_6 = Button(
        frame_baixo,
        command = lambda: controlar('6'), 
        text='', 
        width=3, 
        relief='flat',
        font=('Ivy 20 bold'),
        overrelief=RIDGE,
        bg=darkBlack,)
    b_6.place(x=162, y=76)

    b_7 = Button(
        frame_baixo,
        command = lambda: controlar('7'), 
        text='', 
        width=3, 
        relief='flat',
        font=('Ivy 20 bold'),
        overrelief=RIDGE,
        bg=darkBlack,)
    b_7.place(x=30, y=135)

    b_8 = Button(
        frame_baixo,
        command = lambda: controlar('8'), 
        text='', 
        width=3, 
        relief='flat',
        font=('Ivy 20 bold'),
        overrelief=RIDGE,
        bg=darkBlack,)
    b_8.place(x=96, y=135)

    b_9 = Button(
        frame_baixo,
        command = lambda: controlar('9'), 
        text='', 
        width=3, 
        relief='flat',
        font=('Ivy 20 bold'),
        overrelief=RIDGE,
        bg=darkBlack,)
    b_9.place(x=162, y=135)

# Botão Jogar

play = Button(
    frame_baixo,
    command=start_game, 
    text='PLAY', 
    width=10,
    height=1, 
    relief='raised',
    font=('Ivy 10 bold'),
    overrelief=RIDGE,
    bg=blue,
    fg=white)
play.place(x=82, y=215)


j.mainloop()