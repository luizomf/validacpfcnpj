# Valida CPF e CNPJ com Python
Classe que realiza os cálculos matemáticos para verificar
se um CPF ou CNPJ é válido ou não.
## Utilização
Todos os exemplos estão em `exemplos/exemplo_1.py`.
```
import validacpfcnpj
```
Exemplo 1: Enviando CPF ao instanciar a classe
```
"""
Exemplo 1: Enviando CPF ao instanciar a classe
"""
cpf_cnpj = validacpfcnpj.ValidaCpfCnpj('61166492621')

if cpf_cnpj.valida():
    print('CPF %s é válido e foi formatado.' % cpf_cnpj.formatado)
    print('CPF %s é válido e contém apenas números.' % cpf_cnpj.cpf_cnpj)
else:
    print('CPF inválido.')
```
Exemplo 2: Enviando CNPJ ao instanciar a classe
```
"""
Exemplo 2: Enviando CNPJ ao instanciar a classe
"""
cpf_cnpj = validacpfcnpj.ValidaCpfCnpj('10.191.700/0001-64')

if cpf_cnpj.valida():
    print('CNPJ %s é válido e foi formatado.' % cpf_cnpj.formatado)
    print('CNPJ %s é válido e contém apenas números.' % cpf_cnpj.cpf_cnpj)
else:
    print('CNPJ inválido.')
```
Exemplo 3: Reutilizando a classe validando um CNPJ
```
"""
Exemplo 3: Reutilizando a classe validando um CNPJ
"""
cpf_cnpj.cpf_cnpj = '63.080.648/0001-35'

if cpf_cnpj.valida():
    print('CNPJ %s é válido e foi formatado.' % cpf_cnpj.formatado)
    print('CNPJ %s é válido e contém apenas números.' % cpf_cnpj.cpf_cnpj)
else:
    print('CNPJ inválido.')
```
Exemplo 4: CPF Inválido
```
"""
Exemplo 4: CPF Inválido
"""
cpf_cnpj.cpf_cnpj = '11111111111'

try:
    formatado = cpf_cnpj.formatado
except ValueError:
    print("CPF inválido.")
```
Exemplo 5: CNPJ Inválido
```
"""
Exemplo 5: CNPJ Inválido
"""
cpf_cnpj.cpf_cnpj = '10.191.700/0001-65'

try:
    formatado = cpf_cnpj.formatado
except ValueError:
    print("CNPJ inválido.")
```
