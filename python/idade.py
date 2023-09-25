# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2022.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2023).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, 
# o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.


def Nascimento(nome, ano):
  idade = 2023 - ano
  if (ano == 2022):
      print ('Seu nome é: ', nome)
      print ('Sua idade atual é: ', idade, 'ano')
  else:
      print ('Seu nome é: ', nome)
      print ('Sua idade atual é: ', idade, 'anos')

nome = input('Digite seu nome completo: ')

while True:
  try:
      ano = int(input('Digite seu ano de nascimento: (Entre 1922 e 2022)'))
      if (ano >= 1922 and ano <= 2022):
        Nascimento(nome, ano)
        break
      else:
        print('A data digitada está fora do range, tente novamente!\n')
  except:
    print ('Tipo de dado incorreto, tente novamente')
