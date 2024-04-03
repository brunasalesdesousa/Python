#Essa cláusula captura todo tipo de erro, dando um tratamento comum independentemente de qual seja. Para capturar erros específicos, deve-se informar o tipo. No exemplo anterior, é possível verificar que o erro é do tipo ValueError; assim:

try:
    num = int(input("Digite um número: "))
except ValueError:
    print("Valor inválido")
except:
    print("Outro tipo de erro ocorreu!")


    #Neste caso, podem ser identificados vários tipos de erro, tratando cada um de forma individual.