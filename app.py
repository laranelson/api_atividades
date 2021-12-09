from flask import Flask
from flask_restful import Resource, Api, request
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

# USUARIOS = {
#     'nelson':'123',
#     'alice':'123'
# }

# @auth.verify_password
# def veirificacao(usuario, senha):
#     if not(usuario, senha):
#         return False
#     return USUARIOS.get(usuario) == senha

@auth.verify_password
def verificacao(usuario, senha):
    if not(usuario, senha):
        return False
    return Usuarios.query.filter_by(usuario=usuario, senha=senha).first()

# Criando class Pessoa para poder efetuar o GET, PUT e DELETE
class Pessoa(Resource):
    @auth.login_required # Esse decorado foi incluindo, porque para acessar esse metodo é preciso tá logado
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome':pessoa.nome,
                'idade':pessoa.idade,
                'id':pessoa.id
        }
        except AttributeError:
            response = {
                'status':'error',
                'mensagem':'pessoa não encontrada'
            }
        return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = '{} foi excluído(a) com sucesso!'.format(pessoa.nome)
        pessoa.delete()
        return {'status':'sucesso', 'mensagem':mensagem}

# Criando class para listar todas as pessoas e inserir nova pessoa
class ListarPessoas(Resource):
    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'idade':i.idade} for i in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }
        return response

# Criando class para listar todas as atividades e inserir nova atividade
class ListarAtividades(Resource):
    @auth.login_required
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'pessoa':i.pessoa.nome} for i in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa':atividade.pessoa.nome,
            'nome':atividade.nome,
            'id':atividade.id
        }
        return response

api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListarPessoas, '/pessoa/')
api.add_resource(ListarAtividades, '/atividades/')

if __name__ == '__main__':
    app.run(debug=True)