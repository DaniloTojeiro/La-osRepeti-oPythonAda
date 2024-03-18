"""for i in range(10):
    print(i)""" # 1 parametro

"""for i in range(1, 11):
    print(i)""" # 2 parametros

# 1, 4, 7, 10
"""for i in range(1, 12, 3):
    print(i)"""

soma = 0

for i in range(1, 4):
    nota = float(input(f'Informe a sua nota {i}: '))

    soma = soma + nota

print(soma / 3)