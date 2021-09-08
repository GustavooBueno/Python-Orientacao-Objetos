from abc import ABC, abstractmethod

# Super Classe
class empDomestica(ABC):
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    def getNome(self):
        return self.__nome

    def getTelefone(self):
        return self.__telefone

    @abstractmethod
    def getSalario(self):
        pass

# Classe do diarista
class diarista(empDomestica):
    def __init__(self, nome, telefone, diasTrabalhados, valorPorDia):
        super().__init__(nome, telefone)
        self.__diasTrabalhados = diasTrabalhados
        self.__valorPorDia = valorPorDia

    def setvalorPorDia(self, valorPorDia):
        self.__valorPorDia = valorPorDia 

    def setdiasTrabalhados(self, diasTrabalhados):
        self.__diasTrabalhados = diasTrabalhados 

    def getvalorPorDia(self):
        return self.__valorPorDia

    def getdiasTrabalhados(self):
        return self.__diasTrabalhados

    def getSalario(self):
        return self.__valorPorDia * self.getdiasTrabalhados()

# Classe do mensalista
class mensalista(empDomestica):
    def __init__(self, nome, telefone, valorMensal):
        super().__init__(nome, telefone)
        self.__valorMensal = valorMensal

    def setvalorMensal(self, valorMensal):
        self.__valorMensal = valorMensal

    def getSalario(self):
        return self.__valorMensal

# Classe do horista
class horista(empDomestica):
    def __init__(self, nome, telefone, horasTrabalhadas, valorPorHora):
        super().__init__(nome, telefone)
        self.__valorPorHora = valorPorHora
        self.__horasTrabalhadas = horasTrabalhadas

    def sethorasTrabalhadas(self, horasTrabalhadas):
        self.__horasTrabalhadas = horasTrabalhadas

    def setvalorPorHora(self, valorPorHora):
        self.__valorPorHora = valorPorHora 

    def gethorasTrabalhadas(self):
        return self.__horasTrabalhadas

    def getvalorPorHora(self):
        return self.__valorPorHora

    def getSalario(self):
        return self.__valorPorHora * self.gethorasTrabalhadas()

# Main
if __name__ == "__main__":

    # Opções de empregadas
    emp1 = horista('Maria', 35989987644, 160, 10)
    emp2 = diarista('Paula', 2154321666, 20, 55)
    emp3 = mensalista('Ana', 19984287643, 1000)
    emps = [emp1, emp2, emp3]

    # Imprimindo todas as opções
    for emp in emps:
        print ('Nome: {}\nSalário: {}\nTelefone: {}\n----------------------'.format(emp.getNome(), emp.getSalario(), emp.getTelefone()))

    # Lista com salários
    salario = []
    for i in range (len(emps)):
        salario.append(emps[i].getSalario())

    # Achando o menor salário
    min = min(salario)
    index = salario.index(min)

    # Imprimindo a opção mais barata
    print('\n==== MAIS BARATO ====')
    print ('Nome: {}\nSalário: {}\nTelefone: {}\n'.format(emps[index].getNome(), emps[index].getSalario(), emps[index].getTelefone()))
