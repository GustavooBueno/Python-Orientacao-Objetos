from abc import ABC

class Pessoa(ABC):
    def __init__(self, nome, cpf, endereco, idade):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__idade = idade

    def getNome(self):
        return self.__nome
    
    def getCpf(self):
        return self.__cpf

    def getEndereco(self):
        return self.__endereco

    def getIdade(self):
        return self.__idade

    def printDescricao():
        print('\nCadastros gerais:')
        print(cadastroProfessor)
        print(cadastroAluno)

class Professor(Pessoa):
    def __init__(self, nome, cpf, endereco, idade, titulacao):
        super().__init__(nome, cpf, endereco, idade)
        self.__titulacao = titulacao

    def getTitulacao(self):
        return self.__titulacao
    
    def printDescricao():
        print('\nCadastro professor:')
        print(cadastroProfessor)


class Aluno(Pessoa):
    def __init__(self, nome, cpf, endereco, idade, curso):
        super().__init__(nome, cpf, endereco, idade)
        self.__curso = curso
    
    def getCurso(self):
        return self.__curso

    def printDescricao():
        print('\nCadastro aluno:')
        print(cadastroAluno)

class IdadeInvalida(Exception):
    pass

class TitulacaoInvalida(Exception):
    pass

class CursoInvalido(Exception):
    pass

class CpfDuplicado(Exception):
    pass


if __name__ == '__main__':
    listaProfessor = [('Paulo', 1111111111, 'Rua x', 21, 'mestre'), 
    ('Paulo', 212121, 'Rua x', 21, 'mestre'), 
    ('Cleber', 111111111, 'Rua a', 39, 'mestre'),
    ('João', 43719356809, 'Rua b', 51, 'doutor'),
    ('Renato', 4333333333, 'Rua z', 22, 'doutor'),
    ('Pedro', 66666666, 'Rua 1', 18, 'mestre'),
    ('Antonio', 8432432, 'Rua 2', 40, 'doutor')]

    listaAluno = [('Paulo', 43719356809, 'Rua x', 21, 'CCO'), 
    ('Paulo', 7777777, 'Rua x', 11, 'SIN'), 
    ('Cleber', 99999999999, 'Rua a', 39, 'MAT'),
    ('João', 000000000, 'Rua b', 58, 'CCO'),
    ('Renato', 4535345, 'Rua z', 22, 'SDJH'),
    ('Pedro', 543543535, 'Rua 1', 18, 'SIN'),
    ('Antonio', 43719356809, 'Rua 2', 10, 'MAT')]

    cadastroAluno = {}
    cadastroProfessor = {}

    print('Informações inválidas professor:')
    for nome, cpf, endereco, idade, titulacao in listaProfessor:
        try:
            if titulacao != 'doutor':
                raise TitulacaoInvalida()
            if idade < 30:
                raise IdadeInvalida()
            if cpf in cadastroProfessor:
                raise CpfDuplicado()
        except TitulacaoInvalida:
            print('Titulação inválida: %s' %titulacao)
        except IdadeInvalida:
            print('Idade inválida: %d' %idade)
        except CpfDuplicado:
            print("Cpf %d ja está em uso" % cpf)
        else:
            cadastroProfessor[nome] = cpf


    print('\nInformações inválidas alunos:')
    for nome, cpf, endereco, idade, curso in listaAluno:
        try:
            if curso != 'SIN' and 'CCO':
                raise CursoInvalido()
            if idade < 18:
                raise IdadeInvalida()
            if cpf in cadastroAluno:
                raise CpfDuplicado()
        except IdadeInvalida:
            print('Idade inválida: %d' %idade)
        except CursoInvalido:
            print('Curso inválido: %s' %curso)
        except CpfDuplicado:
            print("Cpf %d ja está em uso" % cpf)
        else:
            cadastroAluno[nome] = cpf

    Aluno.printDescricao()
    Professor.printDescricao()
    Pessoa.printDescricao()


