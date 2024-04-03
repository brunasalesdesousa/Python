#Vamos a alguns exemplos? O comando break interrompe um laço no ponto onde estiver do código, passando a execução do programa para a linha imediatamente posterior ao final do laço.

#Exemplo de aplicação 4: Elabore um programa que solicite ao usuário dez números e efetue a soma, exibindo o resultado. Contudo, se em algum momento o número digitado for 0, deve interromper o laço, mostrando a soma apenas dos valores informados até então.


soma = 0
for i in range(10):
    num = int(input("Digite o " + str(i + 1) + " número: "))
    if num == 0:
        break

    soma += num
print("A soma dos números é", soma)
