#Mostrando o Menu Principal
print('Bem-Vindo ao menu!')
print('1. Estudantes')
print('2. Professores')
print('3. Disciplinas')
print('4. Turmas')
print('5. Mattrículas')
print('0. Sair')
#Coletar a opção escolhida poelo usuário
opcao = input('Digite uma opção válida.')

if opcao == '1' or opcao =='2' or opcao =='3'or opcao =='4'or opcao =='5'or opcao =='0':
        print ('Você escolheu a opção válida {}'.format(opcao))
else:
    print('Você digitou uma opção INVÁLIDA')
        
#Mostrando o menu secundário
print('Menu de operações - Opção {}.'.format(opcao))
print('1. Listar')
print('2. Criar')
print('3. Atualizar')
print('4. Excluir')
print('5. Voltar ao menu')
#Coletar a opção do menu secundário
opcao_secundaria = input('Digite uma opção valida:')
print('Você escolheu a opção secundária {}'.format(opcao_secundaria))

if opcao_secundaria == '1' or opcao_secundaria =='2' or opcao_secundaria =='3'or opcao_secundaria =='4'or opcao_secundaria =='5':
        print ('Você escolheu a opção válida {}'.format(opcao_secundaria))
else:
    print('Você digitou uma opção secundária INVÁLIDA')