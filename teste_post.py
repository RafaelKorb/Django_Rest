import requests

headers = {'Authorization': 'Token 18e499dbd34bf9e0bad31f4b8f31b1f1370d56cc'}

url_base_cursos = "http://localhost:8000/api/v2/cursos/"
url_base_avaliacoes = "http://localhost:8000/api/v2/avaliacoes/"

novo_curso = {
    "titulo": "Gerencia Agil de Projetos com SCRUM",
    "url": "http://www.geekuniversity.com.br/scrum"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)


# Testanto o código de status HTTP 201
assert resultado.status_code == 201

# Testanto se o título do curso retornado é o mesmo do curso informado
assert resultado.json()['titulo'] == novo_curso['titulo']

