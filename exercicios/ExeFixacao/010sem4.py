#Listas com comportamento de vetor
#Exercício de fixação 1: Crie um programa que solicite ao usuário seis números, calculando a média, e mostre uma lista com os números iguais ou acima da média e uma lista com os números abaixo da média.

nums = []
maiores = []
menores = []
soma = 0
for i in range(6):
    num = int (input('Digite um números:'))
    nums.append(num)
    soma += num
media = soma / 6
for num in nums:
    if num >= media:
        maiores.append(num)
    else:
        menores.append(num)
print('A média dos 6 números é', media)
print('O números iguais o maiores são', maiores)
print('O números menores são', menores)


