#VIDEOAULA | Listas | Prof.-Tutor Wellington R Monteiro
#Dica Importante: Verificar documentação do Python

frutas = ['banana', 'maça', 'pêra', 'kiwi','manga', 'morango']
print (frutas)

frutas.reverse()
print(frutas)

frutas.sort()
print(frutas)

lista_antiga = frutas.copy()
frutas.clear()
print(frutas)

frutas.append('framboesa')
print(frutas)

frutas.extend(['abacate', 'mamão'])
print(frutas)

elemento = 'framboesa'
if elemento in frutas:
   resultado = frutas.remove(elemento)
   resultado2= frutas.pop(1)
   print(resultado2)
else:
    print('Este elemento não está na lista')

