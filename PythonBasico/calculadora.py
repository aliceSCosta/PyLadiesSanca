import math

# Calcule o resto da divisão de 10 por 3.
print (10%3)

###############################################################

# Calcule a tabuada do 13.
cont = 0

while cont < 11:
    mult = 13 * cont
    print ('13 x ' + str(cont) + ' = ' + str(mult))

    cont = cont + 1

###############################################################

# Davinir não gosta de ir às aulas. Mas ele é obrigado a comparecer a pelo menos 75% delas. 
# Ele quer saber quantas aulas pode faltar, sabendo que tem duas aulas por semana, durante quatro meses. 
# Ajude o Davinir!

diasAula = (2*4)*4

print ('Você tem ' + str(diasAula) + ' dias de aula')

falta = diasAula*0.25

print('Você pode faltar ' + str(round(falta)) + ' dias')

#################################################################

# Calcule a área de um círculo de raio r=2.

raio = 2
area = math.pi*(raio**2)

print ('A área do círculo é: ' + str(area))

##################################################################

#Quantos segundos há em 3 horas, 23 minutos e 17 segundos?

segundos = 60 #segundo

total = (segundos * 60) * 3 + (segundos * 23) + 17

print('Há ' + str(total) + ' segundos em 3 horas, 23 minutos e 17 segundos')

####################################################################

#Resolva essa expressão:
#100−413⋅(20−5×4)/5

r = (100-413*(20-5*4))/5

print(r)