#Elabore um programa que solicite três números, some-os e exiba o resultado para o usuário.


soma = 0
for i in range(3): #tradução = para i no intervalo / range = intervalo
    num = int(input("Digite o " + str(i + 1) + " número: "))
    soma += num
print("A soma dos números é", soma)

#Estranhou aquele range() na resolução? Ele será uma função bem útil ao trabalharmos com estruturas de repetição.1
