import requests
import jsonpath

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

#resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')
#primeira = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
#nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
#email = jsonpath.jsonpath(avaliacoes.json(), 'results[0].email')
#nota_dada = jsonpath.jsonpath(avaliacoes.json(), 'results[0].avaliacao')


#Todos os nomes das pessoas que avaliaram
#nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
#print(nomes)

#Todas as avaliacoes
#notas = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')
#print(notas)
