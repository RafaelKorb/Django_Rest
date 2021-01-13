import requests

headers = {'Authorization': 'Token 	5a8d720e2c455b42ac408fd96ed5e607629dfeee'}

url_base_cursos = "http://localhost:8000/api/v2/cursos/"
url_base_avaliacoes = "http://localhost:8000/api/v2/avaliacoes/"


resultado = requests.delete(url=f'{url_base_cursos}6/', headers=headers)

# Testando o código HTTP
assert  resultado.status_code == 204

# Testando se o tamanho do conteúdo retornado é 0
assert len(resultado.text) == 0
