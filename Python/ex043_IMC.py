#================formulario=================#
peso = float(input('Digite seu peso: '))
alt = float(input('Digite sua altura: '))
#===========================================#

imc = peso / (alt * alt)
print('O imc dessa pessoa é de {:.1f}'.format(imc))

#============condicionais===================#
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso')
elif imc >= 30 and imc < 40:
    print('Você está com obesidade!')
else:
    print('Você está com obesidade mórbida')
#===========================================#

print('Fim')