# Elabore um algoritmo que possa descobrir, através de perguntas e respostas, 
#em qual área de um restaurante uma pessoa ou grupo de pessoas precisa ser alocada.

# O restaurante tem três áreas: térreo, 1° andar, e área externa.
# Clientes fumantes ou com animais de estimação precisam ser alocadas na área externa.
# Grupos de 5 ou mais precisam ser alocados no 1º andar, pois não dá para juntar mesas no térreo.
# Qualquer outro grupo de pessoas pode ser alocado no térreo. 


fumante = input("Você é fumante? Responda com SIM ou NÃO: ")
animal = input("Você está com um animal de estimação? Responda com SIM ou NÃO: ")
pessoas = int(input("Contando com você, a mesa será para quantas pessoas?: "))

if fumante == "SIM" or animal == "SIM":
    print("Você deve ir para a área externa")
else:
    if pessoas >= 5:
        print("Você deve ir para o 1º andar")
    else:
        print("Você deve ir para o térreo")

