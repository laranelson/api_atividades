from models import Pessoas, Usuarios

def insere_pessoas():
    nome = input('Digite o nome da pessoa: ')
    idade = int(input('Digite a idade da pessoa: '))
    pessoa = Pessoas(nome=nome, idade=idade)
    pessoa.save()
    print(pessoa, idade, 'anos de idade foi cadastrado com sucesso!')

def consulta_pessoas():
    #pessoa = Pessoas.query.all()
    pessoa_old = input('Digite o nome da pessoa: ')
    pessoa = Pessoas.query.filter_by(nome=pessoa_old).first()
    print(pessoa, pessoa.idade, 'anos')

def altera_pessoa():
    global pessoa_old
    pessoa_old = input('Digite o nome da pessoa: ')
    pessoa = Pessoas.query.filter_by(nome=pessoa_old).first()
    pessoa.idade = input('Digite a nova idade: ')
    pessoa.save()

def delete():
    pessoa_old = input('Digite o nome da pessoa para deletar: ')
    pessoa = Pessoas.query.filter_by(nome=pessoa_old).first()
    pessoa.delete()

def insere_usuario(usuario, senha):
    usuario = input('Digite o nome de usuario: ')
    senha = int(input('Crie sua senha: '))
    usuario = Usuarios(usuario=usuario, senha=senha)
    usuario.save()
    print(usuario, 'foi cadastrado com sucesso!')

def listar_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

def alterar_usuario():
    usuario_old = input('Digite o nome da pessoa: ')
    usuario = Usuarios.query.filter_by(usuario=usuario_old).first()
    usuario.senha = input('Digite a nova senha: ')
    usuario.save()

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    #delete()
    #consulta_pessoas()
    #insere_usuario('','')
    #listar_usuarios()
    alterar_usuario()
