import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import validacpfcnpj

"""
Exemplo 1: Enviando CPF ao instanciar a classe
"""
cpf_cnpj = validacpfcnpj.ValidaCpfCnpj('61166492621')

if cpf_cnpj.valida():
    print('CPF %s é válido e foi formatado.' % cpf_cnpj.formatado)
    print('CPF %s é válido e contém apenas números.' % cpf_cnpj.cpf_cnpj)
else:
    print('CPF inválido.')

"""
Exemplo 2: Enviando CNPJ ao instanciar a classe
"""
cpf_cnpj = validacpfcnpj.ValidaCpfCnpj('10.191.700/0001-64')

if cpf_cnpj.valida():
    print('CNPJ %s é válido e foi formatado.' % cpf_cnpj.formatado)
    print('CNPJ %s é válido e contém apenas números.' % cpf_cnpj.cpf_cnpj)
else:
    print('CNPJ inválido.')

"""
Exemplo 3: Reutilizando a classe validando um CNPJ
"""
cpf_cnpj.cpf_cnpj = '63.080.648/0001-35'

if cpf_cnpj.valida():
    print('CNPJ %s é válido e foi formatado.' % cpf_cnpj.formatado)
    print('CNPJ %s é válido e contém apenas números.' % cpf_cnpj.cpf_cnpj)
else:
    print('CNPJ inválido.')

"""
Exemplo 4: CPF Inválido
"""
cpf_cnpj.cpf_cnpj = '11111111111'

try:
    formatado = cpf_cnpj.formatado
except ValueError:
    print("CPF inválido.")

"""
Exemplo 5: CNPJ Inválido
"""
cpf_cnpj.cpf_cnpj = '10.191.700/0001-65'

try:
    formatado = cpf_cnpj.formatado
except ValueError:
    print("CNPJ inválido.")