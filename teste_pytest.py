import requests


class TestCursos:
    headers = {'Authorization': 'Token 5a8d720e2c455b42ac408fd96ed5e607629dfeee'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}3/', headers=self.headers)

        assert resposta.status_code == 200
    
    def test_post_curso(self):
        novo = {
            "titulo": "Curso de Programacao com javinha",
            "url": "http://www.geekuniversity.com.br/javinha"
        }
        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo": "Novo Curso de abacate",
            "url": "http://geekuniversity.com.br/abacate"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}4/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200
    
    def test_put_titulo_curso(self):
        atualizado = {
           "titulo": "Novo Curso banana",
            "url": "http://geekuniversity.com.br/banana"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}4/', headers=self.headers, data=atualizado)

        assert resposta.json()['titulo'] == atualizado['titulo']


    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}4/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0