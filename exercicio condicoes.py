nome = input ('qual o seu nome? ')
idade = int (input('qual a sua idade? '))
if idade < 12:
    print ('%s, você é criança' %nome)
elif idade < 18:
    print('%s, você é adolescente' %nome)
elif idade <60:
    print('%s, você é Adulto' %nome)
else:
    print('%s, você é idoso' %nome)
