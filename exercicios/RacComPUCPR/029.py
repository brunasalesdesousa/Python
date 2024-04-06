#Exemplo de aplicação 3: Dada a lista de dados nums = [1, 4, 23, 11, 8], corra a lista usando um objeto range e imprima cada elemento em uma linha.


nums = [1, 4, 23, 11, 8]
for i in range(len(nums)):
    print(nums[i])

#DICA: Também podemos acessar os elementos pelo índice relativo. No exemplo acima, nums[-1] permitiria acessar o último elemento da lista. Já nums[-2] permitiria acessar o penúltimo elemento, nums[-3] permitiria acessar o antepenúltimo elemento, e assim sucessivamente.

#Veja duas coisas novas neste exemplo:
#Linha 2, função len(): ela permite saber o comprimento (tamanho) de uma lista.
#No exemplo acima, len(nums) resulta em 5, porque nums é uma lista com 5 elementos.
#Esta função também funciona com strings. Assim, len("olá!”) resulta em 4, porque a string “olá!” possui 4 elementos.
#len significa length (comprimento).
#Linha 3: nums[i]permite acessar o i-ésimo elemento de uma lista. Assim:
#nums[0]: acessa o primeiro elemento da lista (valor 1).
#nums[1]: acessa o segundo elemento da lista (valor 4).
#nums[2]: acessa o terceiro elemento da lista (valor 23).
#nums[3]: acessa o quarto elemento da lista (valor 11).
#nums[4]: acessa o quinto elemento da lista (valor 8).
