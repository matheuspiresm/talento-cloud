# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da 
# operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:

# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão


# Criando a função calculadora
def calculadora(primeiroNumero, segundoNumero, operacao):

  if (operacao == 1):
    return primeiroNumero + segundoNumero;

  elif (operacao == 2):
    return primeiroNumero - segundoNumero;

  elif (operacao == 3):
    return primeiroNumero * segundoNumero;

  elif (operacao == 4):
    if (segundoNumero != 0):
      return primeiroNumero / segundoNumero;
    else:
      return 'Operação não realizada, divisão por zero';

  else: return ('Número de Operação inválida');

print('---------- Calculadora ---------- \n');

# Solicitando ao usuário a entrada dos números para o cálculo + o número da operação
primeiroNumero = float(input('Digite o primeiro número: '));
segundoNumero = float(input('Digite o segundo número: '));

# Exibindo para o usuário as opções de operações disponíveis:
print ('\n Escolha uma das operações abaixo digitando somente o número correspondente: \n')
print('1 - Soma');
print('2 - Subtração');
print('3 - Multiplicação');
print('4 - Divisão \n');

operacao = int(input('Digite o número da operação: '));

# Exibindo o resultado a partir das entradas feitas
resultado = calculadora(primeiroNumero, segundoNumero, operacao);

print ('\n O resultado é: ', resultado);
