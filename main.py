from API_4DEVS import cpf, cnpj

print("""
1 - Gerador de CPF
2 - Gerador de CNPJ
    """)

menu = int(input('Escolha uma opção: '))

if menu == 1:
    quant = int(input('Quantidade de CPF: '))
    uf = input('Estado: ')
    resposta = cpf(quant, uf)

if menu == 2:
    quant = int(input('Quantidade de CNPJ: '))
    resposta = cnpj(quant)
