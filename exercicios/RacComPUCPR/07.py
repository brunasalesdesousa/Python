
 #Em Python, o for pode ser usado para iterar (percorrer) por sequências finitas como strings (textos) ou um conjunto pré-definido de valores

nome = input('Digite seu nome:') #perceba que não tem int nem float nem nada porque quando for texto, letras não precisa

for letra in nome: #tradução: para letra em nome:

    print(letra)
    #O laço for faz uma iteração com a string, passando por cada uma de suas letras.