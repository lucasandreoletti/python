#calcular imc

def calc_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input('Digite seu peso atual: '))
altura = float(input('Digite sua altura atual: '))
imc = round(calc_imc(peso, altura),2)

#interpretadores

print('Seu IMC é: %s' % imc)
if imc <=18:
    print('Abaixo do peso ideal')
elif imc <= 18.5 or imc <= 24.9:
    print('Peso ideal')
elif imc <= 25 or imc <= 29.9:
    print('Sobrepeso')
elif imc <= 30 or imc <= 34.9:
    print('Obesidade grau 1')
elif imc <= 35 or imc <= 39.9:
    print('Obesidade grau 2')
else:
    print('Obesidade grau 3 ou Mórbida')