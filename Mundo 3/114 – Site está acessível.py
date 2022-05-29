import requests
url = "http://pudim.com.br/"

try:
    requests.get(url).status_code == 200
    print("O servidor está disponível.")
except:
    print("O servidor está indisponível.")