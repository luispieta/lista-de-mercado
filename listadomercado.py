escolha = ''
lista = []
while escolha.lower() != 'sair':
    print('--------MENU--------')
    print('O que deseja fazer?')
    print('Inserir um item na lista (Inserir)')
    print('Alterar um item da lista (Alterar)')
    print('Excluir um item da lista (Excluir)')
    print('Mostrar itens da lista (Mostrar)')
    print('Quantidade de itens que tem na lista (Quantidade)')
    print('Sair da lista')
    escolha = input('')

    if escolha.lower() == 'inserir':
        inserir = input('Digite o que deseja inserir: ')        
        lista.append(inserir)

    if escolha.lower() == 'alterar':
        alterar = int(input('Digite um número que comece do 0 para alterar: '))
        lista.pop(-alterar)
        item_alterado = input('Digite um novo item: ')
        lista.append(item_alterado)

    if escolha.lower() == 'excluir':
        excluir = input('Digite o que deseja excluir: ')
        lista.remove(excluir)

    if escolha.lower() == 'mostrar':
        print('---ITENS---')
        for itens in lista:
            print(itens)

    if escolha.lower() == 'quantidade':
        quantidade = len(lista)
        print(f'Quantidade de itens na lista {quantidade}')

print('Obrigado!')