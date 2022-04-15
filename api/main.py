from api import cpf, cnpj

print("""
[1] - Gerar CPF.
[2] - Gerar CNPJ.
""")

menu = int(input("Insira a opção: "))

if menu == 1:
	quant = int(input("Insira a quantidade de CPF: "))
	uf = input("Estado: ")
	resposta =  cpf(quant, uf)
elif menu == 2:
	quant = int(input("Insira a quantidade de CNPJ: "))
	resposta = cnpj(quant)
