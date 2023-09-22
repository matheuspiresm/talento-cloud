#Precisamos imprimir um número para cada andar de um hotel de 20 andares. 
#Porém, o dono do hotel é supersticioso e optou por não ter um 13° andar.

# Escreva dois códigos (usando for e while) que imprimam todos os números exceto o número 13.
# Como desafio, imprima eles em ordem decrescente (20, 19, 18...)


#Utilizando for
for cont in range(20, 0, -1):
    if cont == 13:
        continue
    print("Você está no", cont, "º andar")
print("Você está no térreo")

#Utilizando while
cont = 20
while (cont > 0):
  if (cont == 13):
    cont -= 1
  print ("Você está no", cont, "º andar")
  cont -= 1
print ("Você está no térreo")
