from time import sleep
from os import system


# Dicionário de cores no terminal, f antes do nome da cor para fundo, l antes do nome da cor para letra.
cores = {'fbranco': '\033[1;30;47m',
         'fazul': '\033[1;30;46m',
         'fvermelho': '\033[1;30;41m',
         'fverde': '\033[1;34;42m',
         'fpreto': '\033[1;32;48m',
         'limpa': '\033[m',
         'lbranco': '\033[1;38m',
         'lverde': '\033[1;32m',
         'lamarelo': '\033[1;33m',
         'lvermelho': '\033[1;31m',
         'lazul': '\033[4;36m'}


# Declaração de variáveis
busão = []
adquiridos = []
leito = 1
count = 0

# Criando a matriz usando uma lista dentro de outra
for l in range(0, 8):
    linha = []
    for c in range(0, 5):
        if l == 0 and c == 0:
            linha.append('M')
        elif l == 0 or c == 2:
            linha.append('☠')
        else:
            linha.append(leito)
            leito += 1
    busão.append(linha)


# Função limpar terminal
def limpa():
    system('cls')


# Função para printar os lugares do ônibus
def exibir_busão():
    # Título para simular um efeito de profundidade
    print(f'{cores["lbranco"]}⋌{cores["limpa"]}'*54)
    print(
        f'{cores["fpreto"]}{"VISTA AÉREA DA PLANTA DO ÔNIBUS":>42}{cores["limpa"]}')
    print(f'{cores["lbranco"]}⋋{cores["limpa"]}'*54)
    # Formatando a matriz para exibição de reservas, utilizando cores no console
    for l in range(0, 8):
        print(' ')
        for c in range(0, 5):
            if busão[l][c] == '☠':
                print(
                    f'{cores["fbranco"]}{busão[l][c]:^10}{cores["limpa"]}', end=' ')
            elif busão[l][c] == 'M':
                print(
                    f'{cores["fazul"]}{busão[l][c]:^10}{cores["limpa"]}', end=' ')
            elif busão[l][c] == 'X':
                print(
                    f'{cores["fvermelho"]}{busão[l][c]:^10}{cores["limpa"]}', end=' ')
            else:
                print(
                    f'{cores["fverde"]}{busão[l][c]:^10}{cores["limpa"]}', end=' ')
        print()
    print()
    print(
        f'{cores["lazul"]} Obs: Digite um número inteiro que esteja disponível. {cores["limpa"]}')
    print()


# Função menu de opções para o usuario fazer as escolhas
def menu():
    print(f'''
\033[1;32m   .-------------------------------------------------------------.
\033[1;32m  |------..-------------..----------..----------..----------..--.|
\033[1;32m .|       \\             ||          ||          ||          ||  ||
\033[1;32m ||        \\            ||          ||          ||          ||  ||
\033[1;31m ||    ..   ||  _    _  ||    _   _ || _    _   ||    _    _||  ||
\033[1;31m  |    ||   || //   //  ||   //  // ||//   //   ||   //   //|| /||
\033[1;31m  |_.------"''----------''----------''----------''----------''--'|
\033[1;31m  .________________ \033[1;32mBEM VINDO A POCCO BUS JAMAICA\033[m \033[1;31m____________ __|\033[m
\033[1;33m  |  | __ |   _-_   |\033[m \033[1m [1] - Comprar Passagem\033[m      \033[1;33m|      ||==|  |\033[m
\033[1;33m  | )| __ |         |\033[m  \033[1m[2] - Listar Poltronas\033[m      \033[1;33m|      ||==|  |\033[m
\033[1;33m  |  | __ | .'.-.'. |\033[m  \033[1m[3] - Sair\033[m        \033[1;33m.'.-.'.   | __   ||==|.'\033[m
\033[1;33m  '---------'|( )|'----------------------'|( )|'----------""''
\033[1;33m              '-'                          '-'\033[m
''')


while True:
    menu()
    opção = int(
        input(f'{cores["lbranco"]}Digite a opção desejada: {cores["limpa"]}'))
    if opção > 4 or opção < 1:
        limpa()
        print('''\033[1;31m          ___ _ __ _ __ ___  _ __ 
         / _ \ '__| '__/ _ \| '__|
        |  __/ |  | | | (_) | |   
         \___|_|  |_|  \___/|_|
 \033[m''')

        print(f'{cores["lvermelho"]}Por gentiliza, informe apenas opçoes validas.{cores["limpa"]}\n')
        print(input(f'{cores["lbranco"]}Tecle ENTER para retornar ao menu principal {cores["limpa"]}'))
        limpa()
    elif opção == 4:
        limpa()
        print(f'''{cores["lbranco"]}Parabéns, você achou uma opção secreta ao som de \033[4mBob Marley\033[m ♪{cores["limpa"]}

{cores["lamarelo"]}Is This Love{cores["limpa"]}
{cores["lbranco"]}♬♪♬♪♬♪♬♪♬♪♬♪♬♪♬♪♬♪♬♪♬♪♬♪♬♪♬♪♬♪....{cores["limpa"]}

I wanna love you and treat you right
I wanna love you every day and every night
We'll be together with a roof right over our heads
We'll share the shelter of my single bed
We'll share the same room, yeah, but Jah, provides the bread

Is this love, is this love, is this love
Is this love that I'm feeling?
Is this love, is this love, is this love
Is this love that I'm feeling?

{cores["lbranco"]}♬♪♬♪♬♪♬♪♬♪♬♪♬♪♬♪♬♪♬♪♬♪♬♪♬♪♬♪♬♪....{cores["limpa"]}\n''')
        print(input(
            f'{cores["lverde"]}Tecle ENTER para retornar ao menu principal {cores["limpa"]}'))
        limpa()
        continue
    if opção == 1:
        while True:
            limpa()
            exibir_busão()
            try:
                reservada = int(
                    input(f'{cores["lbranco"]}Qual poltrona voce deseja reservar: {cores["limpa"]}'))
                limpa()
                print(
                    f'{cores["lamarelo"]}Aguarde um momento... {cores["limpa"]}\n')
                sleep(0.9)
            except:
                print(
                    f'{cores["lvermelho"]}Opcão invalida! Digite um número de poltrona existente!{cores["limpa"]}')
                sleep(1.2)
                limpa()
            else:
                if adquiridos.count(reservada) == 1:
                    print(
                        f'{cores["lvermelho"]}Poltrona {reservada} não está disponível!{cores["limpa"]}\n')
                else:
                    for l in range(0, 8):
                        for c in range(0, 5):
                            if reservada > 0 and reservada <= 28 and adquiridos.count(reservada) == 0:
                                if reservada == busão[l][c]:
                                    busão[l][c] = 'X'
                                    adquiridos.append(reservada)
                                    count += 1
                                    exibir_busão()
                                    limpa()
                                    exibir_busão()
                                    print(
                                        f'{cores["lverde"]}Poltrona {reservada} reservada com sucesso!{cores["limpa"]}\n')

                if reservada <= 0 or reservada >= 29:
                    print(
                        f'{cores["lvermelho"]}Opcão inválida, escolha opcão válida! {cores["limpa"]}')

                resp = str(input(
                    f'{cores["lbranco"]}Deseja reservar outra poltrona? [s/n] {cores["limpa"]}'))
                if resp in 'Nn':
                    limpa()
                    break

    elif opção == 2:
        while True:
            limpa()
            exibir_busão()
            print(input(
                f'{cores["lbranco"]}Tecle ENTER para retornar ao menu principal: {cores["limpa"]}'))
            limpa()
            break

    elif opção == 3:
        limpa()
        print(
            f'{cores["lazul"]}Gerando compravante de reserva...{cores["limpa"]}')
        sleep(1.0)
        file = open('relatorio.txt', 'w', encoding='utf-8')
        file.write('Relatorio de poltronas reservadas e poltronas disponíveis:\n\n')
        for l in range(0, 8):
            for c in range(0, 5):
                file.write(f'{busão[l][c]:^10}')
            file.write('\n\n')
        file.write("\n\nLegenda:\nNúmeros - Disponíveis\nM - Motorista\n☠ - Corredores\nX - Reservada\n\n\n Obrigado por viajar conosco, fiquem na paz de jah!")
        file.close()
        break
