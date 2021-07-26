numero_atomico = int(input('Número atômico: '))

print('\033[31mProtons: {}'.format(numero_atomico))
print('\033[31mEletrons: {}'.format(numero_atomico))

massa_atomica = int(input('\033[30mMassa atômica: '))

neutrons = massa_atomica - numero_atomico

print('\033[31mNeutrons: {}'.format(neutrons))