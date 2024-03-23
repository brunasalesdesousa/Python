

p = float(input('Qual o preço do produto?'))

d = 5/100
t = d*p
des = p-t

print('Parabéns, você ganhou desconto de {:.2f} reais e seu total ficou {:.2f} reais'.format(t,des))
