#importação do módulo calc.py
import calc
valor1 = input("Digite um valor: ")
valor2 = input("Digite outro valor: ")
#armazenando a soma
soma = calc.somar(valor1, valor2)
print(f"A soma é {soma}")

#ou dessa forma

#importação de funções específica do módulo calc.py
from calc import somar, subtrair
valor1 = input("Digite um valor: ")
valor2 = input("Digite outro valor: ")
#armazenando a soma
soma = somar(valor1, valor2)
#exibindo a soma
print(f"A soma é {soma}")