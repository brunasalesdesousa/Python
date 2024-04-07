#Listas com comportamento de matriz

#Exercício de fixação 4: Crie um programa que efetue a soma de duas matrizes 3x3, sabendo que a soma desse tipo de matriz é uma nova matriz 3x3, sendo cada elemento resultado da soma dos elementos das matrizes na mesma posição. Exemplo:

matrizA = []
matrizB = []
matrizSoma = []
for i in range(3):
    matrizA.append([])
    for _ in range(3):
        num = int(input("Elemento da matriz A: "))
        matrizA[i].append(num)
for i in range(3):
    matrizB.append([])
    for _ in range(3):
        num = int(input("Elemento da matriz B: "))
        matrizB[i].append(num)
for i in range(3):
    matrizSoma.append([])
    for j in range(3):
        num = matrizA[i][j] + matrizB[i][j]
        matrizSoma[i].append(num)
print("Matriz A:", matrizA)
print("Matriz A:", matrizB)
print("Matriz A:", matrizSoma)