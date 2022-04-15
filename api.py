from requests import post

url = r'https://www.4devs.com.br/'

def cpf(quant, uf, url):
	for i in range(0, quant):
		r =  post(url, {'acao': 'gerar_cpf', 'pontuacao':'s'})
		resposta = r.text
		print(resposta)

def cnpj(url, quant):
	for i in range(0, quant):
		r = post(url, {'acao':'gerar_cnpj', 'pontuacao':'s'})
		resposta = r.text
		print(resposta)