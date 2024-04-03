#O comando continue força uma nova iteração a partir do ponto em que o programa se encontra, não sendo executado o resto do laço.

#Exemplo de aplicação 5: Elabore um programa que solicite ao usuário dez números e efetue a multiplicação, exibindo o resultado. No entanto, se em algum momento o número digitado for 0, deve pular esta iteração, para que o valor não seja zerado.

mult = 1
for i in range(10):
    num = int (input('Digite o ' + str(i + 1) + ' número:'))
    if num == 0:
        continue
    mult *= num
    print('A multiplicação do número é', mult)