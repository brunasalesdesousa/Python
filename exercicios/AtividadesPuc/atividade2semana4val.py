
lista_estudantes = []


while True:
 #Mostrando o Menu Principal
 print('Bem-Vindo ao menu!')
 print('1. Estudantes')
 print('2. Professores')
 print('3. Disciplinas')
 print('4. Turmas')
 print('5. Matrículas')
 #Coletar a opção escolhida pelo usuário
 opcao = input('Digite uma opção válida.')

 if opcao == '1':
        print ('Você escolheu a opção válida ESTUDANTE nº {}'.format(opcao))
 elif opcao =='2' or opcao =='3'or opcao =='4'or opcao =='5':
        print ('Opção escolhida EM DESENVOLVIMENTO')
 elif opcao == '0':
        print('Você digitou a opção sair')
        break
 else:
        print('Você digitou uma opção secundária INVÁLIDA')
 while True:
    #Mostrando o menu secundário
    print('Menu de operações - Você escolheu no Menu Principal a opção: {}.'.format(opcao))
    print('1. Incluir')
    print('2. Listar')
    print('3. Atualizar')
    print('4. Excluir')
    print('5. Voltar ao menu')
    #Coletar a opção do menu secundário
    opcao_secundaria = input('Digite uma opção valida:')
    print('Você escolheu: {}'.format(opcao_secundaria))

    if opcao_secundaria == '1':
       print ('Você escolheu a opção INCLUIR nº {}'.format(opcao_secundaria))
       codigo = int(input('Digite o código do estudante: '))
       nome = input('Digite seu nome do estudante completo:')
       cpf = input('Digite o CPF do estudante: ')

       dicionario_estudante = {}
       dicionario_estudante['cod_estudante'] = codigo
       dicionario_estudante['nome_estudante'] = nome
       dicionario_estudante['cpf'] = cpf
       lista_estudantes.append(dicionario_estudante)
    elif opcao_secundaria =='2':   
       print (lista_estudantes) 
       
       if len(lista_estudantes) == 0:
        print ('Não há estudantes cadastrados')
       else:
        for estudante in lista_estudantes:  
         print (estudante) 
    elif opcao_secundaria =='3':
       print('Você escolheu atualizar estudante da lista')
       codigo_para_atualizar = int(input('Digite o código do estudante que deseja atualizar: '))
       estudante_atualizado = None
       for dicionario_estudante in lista_estudantes:
           if dicionario_estudante['cod_estudante'] == estudante_atualizado:
               estudante_atualizado = dicionario_estudante
               break
       if estudante_atualizado is None:
           print('Estudante {} não encontrado'.format(codigo_para_atualizar))
       else:
           estudante_atualizado['cod_estudante'] = int(input('Digite o novo código do estudante: '))
           estudante_atualizado['nome_estudante'] = input('Digite o novo nome do estudante: ')
           estudante_atualizado['cpf'] = input('Digite o novo cpf do estudante: ')

           

    elif opcao_secundaria =='4':
        print('Você escolheu excluir estudante da lista')   
        codigo_para_excluir = int(input('Digite o código do estudante que deseja excluir: '))
        estudante_removido = None
        for dicionario_estudante in lista_estudantes:
            if dicionario_estudante['cod_estudante'] == codigo_para_excluir:
                estudante_removido = dicionario_estudante
                break
        lista_estudantes.remove(estudante_removido)   
    elif opcao_secundaria =='5': 
       print('Você escolheu voltar ao Menu Principal')
       break
    else:
       print('Você digitou uma opção INVÁLIDA')