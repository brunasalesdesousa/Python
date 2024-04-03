#Exemplo de aplicação 7: Elabore um programa que solicite um número inteiro ao usuário, validando e imprimindo esse número.


while True:
    try:
        num = int(input("Digite um número: "))
        break
    except ValueError:
        print("Valor inválido")
print("Número validado:", num)

#É importante perceber neste exemplo que, mesmo entrando um formato válido de número (como é o caso do número 3.4), temos uma exceção. Isto acontece porque 3.4 não é um número inteiro, que é o que estamos validando neste código.