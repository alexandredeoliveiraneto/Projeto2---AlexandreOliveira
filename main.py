# ------função rodotrem-----------#
def rodotrem():
    while True:
        peso = float(input('qual seu peso na balança?'))
        if peso > 74:
            excesso = peso - 74
            for i in range(1, 5, 1):
                print('          |       ')
            print('          V       ')
            print('ta com excesso volta pra tirar {} toneladas'.format(excesso))
            for i in range(1, 5, 1):
                print('          |       ')
            print('          V       ')
            print('-----------processo encerrado----------')
            print('-----------processo encerrado----------')
            print('-----------processo encerrado----------')
            print('---------------------------------------')
            print('---------------------------------------')
            print('---------------------------------------')
            print('-----------iniciando processo----------')
            print('-----------iniciando processo----------')
            print('-----------iniciando processo----------')
            break
        elif peso <= 72:
            diferença = 74 - peso
            for i in range(1, 5, 1):
                print('          |       ')
            print('          V       ')
            print('peso muito abaixo pode voltar pra completar {} toneladas'.format(diferença))
            for i in range(1, 5, 1):
                print('          |       ')
            print('          V       ')
            print('-----------processo encerrado----------')
            print('-----------processo encerrado----------')
            print('-----------processo encerrado----------')
            print('---------------------------------------')
            print('---------------------------------------')
            print('---------------------------------------')
            print('-----------iniciando processo----------')
            print('-----------iniciando processo----------')
            print('-----------iniciando processo----------')
            break
        else:
            for i in range(1, 5, 1):
                print('          |       ')
            print('          V       ')
            print('RETIRE SUA NOTA FISCAL AO LADO')
            for i in range(1, 5, 1):
                print('          |       ')
            print('          V       ')
            print('-----------processo encerrado----------')
            print('-----------processo encerrado----------')
            print('-----------processo encerrado----------')
            print('---------------------------------------')
            print('---------------------------------------')
            print('---------------------------------------')
            print('-----------iniciando processo----------')
            print('-----------iniciando processo----------')
            print('-----------iniciando processo----------')
            break


# -----função truck-------#
def truck():
    while True:
        peso = float(input('qual seu peso na balança?'))
        if peso > 31.5:
            excesso = peso - 31.5
            for i in range(1, 5, 1):
                print('          |       ')
            print('          V       ')
            print('ta com excesso volta pra tirar {} toneladas'.format(excesso))
            for i in range(1, 5, 1):
                print('          |       ')
            print('          V       ')
            print('-----------processo encerrado----------')
            print('-----------processo encerrado----------')
            print('-----------processo encerrado----------')
            print('---------------------------------------')
            print('---------------------------------------')
            print('---------------------------------------')
            print('-----------iniciando processo----------')
            print('-----------iniciando processo----------')
            print('-----------iniciando processo----------')
            break
        elif peso <= 29:
            diferença = 31.5 - peso
            for i in range(1, 5, 1):
                print('          |       ')
            print('          V       ')
            print('peso muito abaixo pode voltar pra completar {} toneladas'.format(diferença))
            for i in range(1, 5, 1):
                print('          |       ')
            print('          V       ')
            print('-----------processo encerrado----------')
            print('-----------processo encerrado----------')
            print('-----------processo encerrado----------')
            print('---------------------------------------')
            print('---------------------------------------')
            print('---------------------------------------')
            print('-----------iniciando processo----------')
            print('-----------iniciando processo----------')
            print('-----------iniciando processo----------')
            break
        else:
            for i in range(1, 5, 1):
                print('          |       ')
            print('          V       ')
            print('RETIRE SUA NOTA FISCAL AO LADO')
            for i in range(1, 5, 1):
                print('          |       ')
            print('          V       ')
            print('-----------processo encerrado----------')
            print('-----------processo encerrado----------')
            print('-----------processo encerrado----------')
            print('---------------------------------------')
            print('---------------------------------------')
            print('---------------------------------------')
            print('-----------iniciando processo----------')
            print('-----------iniciando processo----------')
            print('-----------iniciando processo----------')
            break


# --------função vanderleia----------#
def vanderleia():
    while True:
        peso = float(input('qual seu peso na balança?'))
        if peso > 57:
            excesso = peso - 57
            for i in range(1, 5, 1):
                print('          |       ')
            print('          V       ')
            print('ta com excesso volta pra tirar {} toneladas'.format(excesso))
            for i in range(1, 5, 1):
                print('          |       ')
            print('          V       ')
            print('-----------processo encerrado----------')
            print('-----------processo encerrado----------')
            print('-----------processo encerrado----------')
            print('---------------------------------------')
            print('---------------------------------------')
            print('---------------------------------------')
            print('-----------iniciando processo----------')
            print('-----------iniciando processo----------')
            print('-----------iniciando processo----------')
            break
        elif peso <= 55:
            diferença = 57 - peso
            for i in range(1, 5, 1):
                print('          |       ')
            print('          V       ')
            print('peso muito abaixo pode voltar pra completar {} toneladas'.format(diferença))
            for i in range(1, 5, 1):
                print('          |       ')
            print('          V       ')
            print('-----------processo encerrado----------')
            print('-----------processo encerrado----------')
            print('-----------processo encerrado----------')
            print('---------------------------------------')
            print('---------------------------------------')
            print('---------------------------------------')
            print('-----------iniciando processo----------')
            print('-----------iniciando processo----------')
            print('-----------iniciando processo----------')
            break
        else:
            for i in range(1, 5, 1):
                print('          |       ')
            print('          V       ')
            print('RETIRE SUA NOTA FISCAL AO LADO')
            for i in range(1, 5, 1):
                print('          |       ')
            print('          V       ')
            print('-----------processo encerrado----------')
            print('-----------processo encerrado----------')
            print('-----------processo encerrado----------')
            print('---------------------------------------')
            print('---------------------------------------')
            print('---------------------------------------')
            print('-----------iniciando processo----------')
            print('-----------iniciando processo----------')
            print('-----------iniciando processo----------')
            break


# -------programa principal--------#
# programa que verifica se o caminhão esta com peso correto, excesso ou peso baixo e diz quanto retirar ou completar se for o caso.
# esse programa resolveria o problema de liberar nota com excesso...
while True:
    print('BOM DIA MOTORISTA, VAMOS RETIRAR SUA NOTA FISCAL!!')
    print('         --------------------------')
    print('        | 1 -      rodotrem 74 TON|')
    print('        |------------------------ |')
    print('        | 2 -       truck 31.5 TON|')
    print('        |-------------------------|')
    print('        | 3 -    vanderleia 57 TON|')
    print('         --------------------------')
    tipo = input('digite o número do seu caminhao?')
    if tipo == '1':
        rodotrem()

    elif tipo == '2':
        truck()

    elif tipo == '3':
        vanderleia()

    else:
        print('opção inválida')