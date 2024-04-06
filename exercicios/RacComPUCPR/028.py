
#Exemplo de aplicação 2: Elabore um programa que solicite ao usuário cinco números e exiba duas listas separadas: uma contendo somente números pares e outra contendo somente números ímpares. 

pares = []
impares = []
for i in range(5):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print("Números pares:", pares, "- Números ímpares:", impares)

#No algoritmo acima, nós coletamos cinco números do usuário e os separamos em duas listas: uma para números pares e outra para números ímpares.
#Linhas 1 e 2: Iniciamos criando duas listas vazias, pares e impares, que vão armazenar os números pares e ímpares, respectivamente.
#Linha 3: Entramos em um laço "for" que vai se repetir cinco vezes (de 0 a 4).
#Linha 4: Dentro do laço, pedimos para o usuário inserir um número inteiro, que é armazenado na variável num.
#Linha 5: Verificamos se o número é par, usando a condição num % 2 == 0 (um número é par se o resto da sua divisão por 2 é igual a zero).
#Linha 6: Se a condição for verdadeira (ou seja, num é par), adicionamos num à lista pares usando o método append().
#Linhas 7 e 8: Se a condição for falsa (ou seja, num é ímpar), adicionamos num à lista impares.
#Linha 9: Após a execução do laço "for", imprimimos as listas pares e impares.