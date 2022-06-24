import sys

import dns.resolver

# Objeto para fazer as requisições e pegar as INFO
resolver = dns.resolver.Resolver()

# lista de subdomínios - criado no proprio app - teste
# wordlist = ['acceptatie', 'access', 'accounting', 'accounts', 'ad', 'adm', 'admin', 'administrator', 'ads', 'adserver',
           #  'advanced', 'dvwa', 'affiliate', 'affiliates', 'agenda', 'alpha', 'alumni', 'analytics', 'shop']


# como vamo fazer esse app funcionar pelo terminal, precisamos adicionar os args para que o usuário possa utilizar
try:
    alvo = sys.argv[1]  # site a ter o DNS enumerado
    lista_sub = sys.argv[2]  # lista de subdomínios
except:
    print("Falta argumentos -- Modo de uso: python3 DnsComPyhton.py 'dominio' 'lista de subdominio'")
    sys.exit()  # Força o programa a fechar

# pegando lista de um arquivo externo
try:
    lista = open(lista_sub, 'r').read().splitlines()  # .read().splitlines() para pular linhas do arquivo
except:
    print("Lista não encontrada - Verificar nome do arquivo")


for subd in lista:
    try:
        sub_alvo = "{}.{}".format(subd, alvo)
        resultados = resolver.resolve(sub_alvo, "A")

        for resultado in resultados:
            print(sub_alvo, ": ", resultado)  # mostra todos os IP's que o domínio aponta

    except Exception as e:
        pass
        # print("Subdomínio não exite")
        # print(e) # caso necessário mostra o erro
