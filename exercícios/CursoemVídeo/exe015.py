

d = int(input('Quanto dias alugado? '))
km = float(input('Quantos km rodados? '))

dt = d*60
kt = km*0.15
tt = dt+kt

print('O total a pagar é de R$ {:.2f}'.format(tt))