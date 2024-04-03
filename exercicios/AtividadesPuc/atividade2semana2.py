#Mostrando o Menu Principal
print('Bem-Vindo ao menu!')
print('1. Estudantes')
print('2. Professores')
print('3. Disciplinas')
print('4. Turmas')
print('5. Matrículas')
print('0. Sair')
#Coletar a opção escolhida poelo usuário
opcao = int(input('Digite uma opção válida.'))

if opcao >= 0 and opcao <= 5:
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


#Veja que a opção de if só foi válida porque estamos trabalhando com int - converteu para número.
