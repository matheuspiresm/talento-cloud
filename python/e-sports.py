/#Num torneio de e-sports é necessário que todos os integrantes da mesma equipe tenham etiquetas que os identifiquem. 
#Por exemplo, se o nome da equipe é “Os Lutadores”, o primeiro membro deve ter uma etiqueta “Os Lutadores – 1", 
#o segundo membro “Os Lutadores – 2", e assim pela frente.

#Elabore um algoritmo que permita ao usuário inserir o nome da equipe, e imprime 
#etiquetas para os 5 membros da equipe seguindo o exemplo mostrado acima.


equipe = input("Digite o nome da equipe: ")
cont = 1

while cont <= 5:
    print(equipe, "-", cont)
    cont += 1
