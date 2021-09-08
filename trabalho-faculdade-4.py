class Disciplina:

    def __init__(self, titulo, aluno, curso, nroMateria, codigo, cargaHoraria):
        self.__titulo = titulo
        self.__aluno = aluno
        self.__curso = curso
        self.__nroMateria = nroMateria
        self.__codigo = codigo
        self.__cargaHoraria = cargaHoraria

        aluno.addDisciplina(self)

    def getCargaHoraria(self):
        return self.__cargaHoraria

    def getTitulo(self):
        return self.__titulo
    
    def getCodigo(self):
        return self.__codigo

    def getAluno(self):
        return self.__aluno

    def getCurso(self):
        return self.__curso
        
    def getNroMateria(self):
        return self.__nroMateria        

class Curso:

    def __init__(self, titulo, aluno, ano):
        self.__titulo = titulo
        self.__aluno = aluno
        self.__ano = ano

        self.__materia = []

        aluno.addCurso(self)

    def getTitulo(self):
        return self.__titulo

    def getCodigo(self):
        return self.__codigo

    def getAluno(self):
        return self.__aluno

    def getAno(self):
        return self.__ano

    def getMateria(self):
        return self.__materia       

    def addMateria(self, titulo, codigo, cargaHoraria, Aluno=None):
        if Aluno is None:
            Aluno = self.__aluno        
        nroMateria = len(self.__materia)
        disciplina = Disciplina(titulo, Aluno, self, nroMateria, codigo, cargaHoraria)
        self.__materia.append(disciplina)

class Aluno:

    def __init__(self, nome, nroMatric):
        self.__nome = nome
        self.__nroMatric = nroMatric

        self.__Cursos = []
        self.__disciplinas = []

    def getNome(self):
        return self.__nome

    def getNroMatric(self):
        return self.__nroMatric

    def getCursos(self):
        return self.__Cursos

    def getDisciplinas(self):
        return self.__disciplinas        

    def addCurso(self, curso):
        self.__Cursos.append(curso)

    def addDisciplina(self, disciplina):
        self.__disciplinas.append(disciplina)

class Grade:

    def __init__(self, nome, ano):
        self.__nome = nome
        self.__ano = ano

        self.__disciplinas = []

    def getAno(self):
        return self.__ano

    def getNome(self):
        return self.__nome

    def getDisciplinas(self):
        return self.__disciplinas

    def addDisciplina(self, disciplina):
        self.__disciplinas.append(disciplina)


if __name__ == "__main__":
    listaCursos = []

    alu1 = Aluno('Gustavo', 2020008823)
    Curso1 = Curso('Sistemas de Informação', alu1, 2020)
    alu1.addCurso(Curso1)
    Curso1.addMateria('Algoritmo e Estrutura de Dados', 'COM112', 48)
    Curso1.addMateria('Orientação a Objetos', 'COM220', 32)
    Curso1.addMateria('Engenharia de Software', 'COM210', 48) 
    listaCursos.append(Curso1)


    alu2 = Aluno('João', 2020007456)
    Curso2 = Curso('Engenharia Mecânica', alu2, 2020)
    alu2.addCurso(Curso2)
    Curso2.addMateria('Matematica Discreta', 'MAT017', 64)
    Curso2.addMateria('Probabilidade e Estatistica', 'MAT013', 64)
    Curso2.addMateria('Calculo 3', 'MAT157', 48)
    listaCursos.append(Curso2)

    listaAlunos = [alu1, alu2]

    # Criar uma Grade com as disciplinas do Curso "Programação"
    Grade1 = Grade('Programação', 2020)
    for Disciplina in Curso1.getMateria():
        Grade1.addDisciplina(Disciplina)
    print('------------------------')
    print('{} {}:'.format(Grade1.getNome(), Grade1.getAno()))
    for Disciplina in Grade1.getDisciplinas():
        print('{} {}h ({})'.format(Disciplina.getTitulo(), Disciplina.getCargaHoraria(), Disciplina.getCodigo()))
    print('------------------------\n')

     # Criar uma Grade com as disciplinas do Curso "Engenharia"
    Grade4 = Grade('Engenharia', 2020)
    for Disciplina in Curso2.getMateria():
        Grade4.addDisciplina(Disciplina)
    print('------------------------')
    print('{} {}:'.format(Grade4.getNome(), Grade4.getAno()))
    for Disciplina in Grade4.getDisciplinas():
        print('{} {}h ({})'.format(Disciplina.getTitulo(), Disciplina.getCargaHoraria(), Disciplina.getCodigo()))
    print('------------------------\n')

    # Criar uma Grade contendo uma disciplina de cada Curso
    Grade3 = Grade('Grade Alternativa', 2020)
    for Curso in listaCursos:
        Disciplinas = Curso.getMateria()
        Grade3.addDisciplina(Disciplinas[0])
    print('------------------------')
    print(Grade3.getNome(), Grade3.getAno())
    for Disciplina in Grade3.getDisciplinas():
        print('{} {}h ({})'.format(Disciplina.getTitulo(), Disciplina.getCargaHoraria(), Disciplina.getCodigo()))
    print('------------------------')

    # Criar uma Grade com todas as disciplinas de um aluno especifico
    print('Opções:   [0] {} [1] {}'.format(alu1.getNome(), alu2.getNome()))
    escolha = int(input('Escolha: '))
    Grade2 = Grade('Grade do {} da matrícula {}:'.format(listaAlunos[escolha].getNome(), listaAlunos[escolha].getNroMatric()), 2020)
    print('------------------------')
    for Disciplina in listaAlunos[escolha].getDisciplinas():
        Grade2.addDisciplina(Disciplina)
    print('{}\nAno:{}'.format(Grade2.getNome(), Grade2.getAno()))
    for Disciplina in Grade2.getDisciplinas():
        print('{} {}h ({})'.format(Disciplina.getTitulo(), Disciplina.getCargaHoraria(), Disciplina.getCodigo()))
    print('------------------------\n')



    #CRIAR HISTORICO
    #VER COMO FAZER CARGA HORARIA

    #DUVIDAS QUE SURGIRAM: 
    #COMO CRIAR UMA OPÇÃO [] 
    #COMO FAZER PARA VOLTAR EM UM PRINT EX: PRINT('Opções:  [0]  [1]') --> SE A PESSOA DIGITAR 3 RETORNA PRO PRINT

    
