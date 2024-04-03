#Este mesmo exemplo pode ser implementado fazendo uso de uma condição infinita, com o comando de controle de fluxo break.

soma = 0
num = -1
while True:
    num = int(input("Digite um número para somar (0 finaliza): "))
    if num == 0:
        break;
    soma += num
print("A soma dos números é ", soma)

#Percebeu aquele “while True”? Ele é um laço infinito: como True é sempre verdade, precisamos forçar a saída do laço dentro dele: daí a presença do break. Vejamos uma explicação mais aprofundada sobre o que o código acima faz – veja principalmente as mudanças dentro do passo 3:

#Inicializamos a variável soma com o valor 0. Essa variável será usada para armazenar o resultado da soma dos números.
#Inicializamos a variável num com o valor -1. Essa variável armazena o número digitado por nós a cada iteração.
#Entramos no laço "enquanto" (while) com a condição True, o que significa que o laço continuará até que seja interrompido explicitamente dentro dele.
#Dentro do laço, solicitamos um número inteiro e armazenamos esse valor na variável num.
#Se num for igual a 0, usamos o comando break para sair do laço imediatamente, sem atualizar a soma.
#Se num for diferente de 0, adicionamos o valor de num à variável soma.
#Após o término do laço (quando digitarmos 0), o algoritmo imprime a mensagem "A soma dos números é ", seguida pelo valor da variável soma, que contém o resultado da soma dos números fornecidos por nós.
#Da mesma forma, podem ser usados os comandos continue e pass com o comando while.