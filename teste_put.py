import requests

headers = {'Authorization': 'Token 	5a8d720e2c455b42ac408fd96ed5e607629dfeee'}

url_base_cursos = "http://localhost:8000/api/v2/cursos/"
url_base_avaliacoes = "http://localhost:8000/api/v2/avaliacoes/"


curso_atualizado = {
    "titulo": "novo curso de Linux :O",
    "url": "http://www.puttest.com.br/pinguim"
}


# Buscando o curso com ID 6
#curso = requests.get(url=f'{url_base_cursos}6/', headers=headers)
#print(curso.json())


resultado = requests.put(url=f'{url_base_cursos}6/', headers=headers, data=curso_atualizado)

# Testando o código de status
assert resultado.status_code == 200

# Testando o título
assert resultado.json()['titulo'] == curso_atualizado['titulo']

