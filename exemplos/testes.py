# Apenas alguns testes, por favor, ignore.
import validacpfcnpj

# 81.684.901/0001-41
# 00.757.144/0001-97
cpf_cnpj = validacpfcnpj.ValidaCpfCnpj()

for i in range(10):
    sequencia_cnpj = str(i) * 14

    cpf_cnpj.cpf_cnpj = sequencia_cnpj

    if cpf_cnpj.valida():
        print('CNPJ Válido')
    else:
        print('CNPJ %s Inválido.' % cpf_cnpj.cpf_cnpj)

    sequencia_cpf = str(i) * 11
    cpf_cnpj.cpf_cnpj = sequencia_cpf

    if cpf_cnpj.valida():
        print('CPF Válido')
    else:
        print('CPF %s Inválido.' % cpf_cnpj.cpf_cnpj)

cpf_cnpj.cpf_cnpj = '00.757.144/0001-97'

if cpf_cnpj.valida():
    print('CNPJ %s Válido.' % cpf_cnpj.cpf_cnpj)
else:
    print('CNPJ %s Inválido.' % cpf_cnpj.cpf_cnpj)

cpf_cnpj.cpf_cnpj = '61166492621'

if cpf_cnpj.valida():
    print('CPF %s Válido.' % cpf_cnpj.cpf_cnpj)
else:
    print('CPF %s Inválido.' % cpf_cnpj.cpf_cnpj)


