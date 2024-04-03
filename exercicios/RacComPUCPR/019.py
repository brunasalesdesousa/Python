#O que acha de testar o código abaixo e digitar de novo “banana” como sendo um número?


try:
    num = int(input("Digite um número: "))
except:
    print("Valor inválido")


#Neste caso, em vez de disparar a exceção, ela é capturada pela cláusula except, mostrando a mensagem de “valor inválido”.