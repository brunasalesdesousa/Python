#Exemplo de aplicação 8: Elabore um programa que solicite um número decimal ao usuário, validando e imprimindo esse número.


while True:
    try:
        num = float(input("Digite um número decimal: "))
        break
    except ValueError:
        print("Valor inválido")
print("Número validado:", num)


#Além da validação pelo tipo de dado correto, é possível validar valores de acordo com determinado critério. Neste caso, a saída do laço só deve ser chamada após o critério ser satisfeito.