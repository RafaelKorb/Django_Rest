import requests

headers = {'Authorization': 'Token 18e499dbd34bf9e0bad31f4b8f31b1f1370d56cc'}

url_base_cursos = "http://localhost:8000/api/v2/cursos/"
url_base_avaliacoes = "http://localhost:8000/api/v2/avaliacoes/"

resultado = requests.get(url=url_base_cursos, headers=headers)

print(resultado.json())


#Testando se o endpoint esta correto
assert resultado.status_code == 200