import requests


#GET Avaliacoes

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# Acessando codigo de status HTTP
# print(avaliacoes.status_code)


#Acessando od dados da resposta
#print(avaliacoes.json())


# Acessando a próxima pagina de resultados
# print(avaliacoes.json()['next'])


# Acessando os resultados desta página (lista)
# print(avaliacoes.json()['results'])


# Acessando o primeiro elemento da lista de resultados
# print(avaliacoes.json()['results'][0])


# Acessando o primeiro elemento da lista de resultados
# print(avaliacoes.json()['results'][0]['nome'])


#GET Avaliacao

avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/2/')
#print(avaliacao.json())



#GET Cursos

headers = {'Authorization': 'Token 18e499dbd34bf9e0bad31f4b8f31b1f1370d56cc'}

cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)
print(cursos.json())
