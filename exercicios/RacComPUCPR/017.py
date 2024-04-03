#Exemplo de aplicação 6: Elabore um programa que solicite ao usuário que digite indefinidamente números e efetue a soma, parando apenas quando o usuário digitar o número 0.

soma = 0
num = -1
while num != 0: #while = enquanto
    num = int(input("Digite um número para somar (0 finaliza): "))
    soma += num
print("A soma dos números é ", soma)

#Vejamos como o algoritmo acima funciona:

#Inicializamos a variável soma com o valor 0. Essa variável será usada para armazenar o resultado da soma dos números.
#Inicializamos a variável num com o valor -1. Essa variável armazena o número digitado por nós a cada iteração.
#Entramos no laço "enquanto" (while) que se repete enquanto num for diferente de 0:
#Solicitamos um número inteiro e armazenamos esse valor na variável num.
#Se num for diferente de 0, adicionamos o valor de num à variável soma.
#Se num for 0, o laço "enquanto" será encerrado, e a soma não será atualizada.
#Após o término do laço (quando digitarmos 0), o algoritmo imprime a mensagem "A soma dos números é ", seguida pelo valor da variável soma, que contém o resultado da soma dos números fornecidos por nós.