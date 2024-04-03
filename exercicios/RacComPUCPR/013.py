#Exemplo de aplicação 3: Elabore um programa que calcule o fatorial de um número, exibindo a informação de como é feito o cálculo. Exemplo: “O valor do fatorial de 5 é igual a 120. Expressão: 5*4*3*2*1”. 

fatorial = 1
expressao = "Expressão: "
num = int(input("Digite um número para o cálculo do fatorial: "))
for i in range(num, 0, -1):
    fatorial *= i
    expressao += str(i)
    if i > 1:
        expressao += " * "
print("O valor do fatorial de", num, "é", fatorial, expressao)


#Vejamos como esta resolução funciona:

#Primeiro, inicializamos a variável fatorial com o valor 1. Esta variável será usada para armazenar o resultado do cálculo do fatorial.
#Depois, inicializamos a variável expressao com a string "Expressão: ". Ela será usada para construir e exibir a expressão matemática do fatorial.
#Depois, pedimos ao usuário um número inteiro num para calcular o fatorial e armazenamos esse valor na variável num.
#O algoritmo entra no laço "para" (for) que itera de num até 1, decrementando 1 a cada iteração (range(num, 0, -1)).
#Em cada iteração, multiplicamos o valor atual de fatorial pelo valor de i (índice da iteração) e atualizamos a variável fatorial com o resultado.
#Adicionamos o valor de i convertido para string à variável expressao.
#Se i for maior que 1, adiciona o símbolo " * " à variável expressao. Isso cria a expressão matemática do fatorial.
#Após o término do laço, o algoritmo imprime a mensagem contendo o valor do fatorial de num, o resultado do cálculo e a expressão matemática.
