fila=[]
menu= 's'
while menu == 's'
    print('Gestao de refeitorio')
    print('digite 1 para adicionar alguem no fim da fila')
    print('digite 2 para adicionar alguem em uma posicao da fila')
    print('digite 3 para remover alguem da fila')
    print('digite 4 para remover alguem em uma posicao da fila')
    print('digite 'e' para sair')

    
    novo_nome= input('digite um nome para ser adicionado a fila:')

    fila.append(novo_nome)


    for nome in fila:
        print(nome)

        menu=input('deseja adicionar mais um nome? (s/n)')
        