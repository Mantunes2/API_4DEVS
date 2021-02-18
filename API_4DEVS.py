from requests import post

def cpf(quant, uf):
    for i in range(0, quant):
        req = post('https://www.4devs.com.br/ferramentas_online.php', {'acao':'gerar_cpf','pontuacao':'s','cpf_estado':uf})
        resposta = req.text
        print(resposta)


def cnpj(quant):
    for i in range(0, quant):
        req = post('https://www.4devs.com.br/ferramentas_online.php', {'acao':'gerar_cpf','pontuacao':'s'})
        resposta = req.text
        print(resposta)
