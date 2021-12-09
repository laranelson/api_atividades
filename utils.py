from models import Pessoas

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

if __name__ == '__main__':
    insere_pessoas()
    #altera_pessoa()
    #delete()
    #consulta_pessoas()
