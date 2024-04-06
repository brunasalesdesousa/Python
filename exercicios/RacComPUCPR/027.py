#E se quiséssemos adicionar 10 elementos? 20? 50? Para que possamos adicionar os itens dinamicamente em uma lista existe um segredo para isto: o método append. Veja um exemplo:


nums = []
for i in range(5):
    num = int(input("Digite um número: "))
    nums.append(num)
print(nums)

#DICA: Use o método .append() para incluir novos valores em uma lista.

#Dessa forma, independentemente da quantidade de elementos, a lista será populada corretamente. Até porque, geralmente, uma lista pode conter uma quantidade indefinida de elementos. O que acha de mudar aquele range(5) por um range(3) para ver o que acontece? Tente mudar para range(8), também. Viu que não deu nenhum erro nestes casos?

