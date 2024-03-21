n = input('Digite algo:')
          
print('O tipo primitivo desse valor é:',type(n))
print('É numérico?', n.isnumeric())
print('É todo em letra maiúscula?', n.isupper())
print('Tem somente letras?', n.isalpha())
print('Tem letras e números?', n.isalnum())
