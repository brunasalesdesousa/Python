 
estudantes =[]

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
       nome = input('Digite seu nome completo:')
       estudantes.append(nome)
    elif opcao_secundaria =='2':   
       print ('Listagem: {}'.format(nome [1])) 
       
       if len(estudantes)== 0:
        print ('Não há estudantes cadastrados')
       else:
        for estudante in estudantes:  
         print (estudante) 
    elif opcao_secundaria =='3'or opcao_secundaria =='4':
       print('Opção escolhida EM DESENVOLVIMENTO')
    elif opcao_secundaria =='5': 
       print('Você escolheu voltar ao Menu Principal')
       break
    else:
       print('Você digitou uma opção INVÁLIDA')