class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def __eq__(self, other):
        return self.__cpu == other.cpu

    def __ne__(self, other):
        return self.__cpu != other.cpu

    def __lt__(self, other):
        return self.__cpu < other.cpu

    def __gt__(self, other):
        return self.__cpu > other.cpu

    def __le__(self, other):
        return self.__cpu <= other.cpu

    def __ge__(self, other):
        return self.__cpu >= other.cpu

    """arithmetical calculation"""

    def make_computations(self):
        multiplication = self.cpu * self.memory
        addition = self.cpu + self.memory
        division = self.cpu / self.memory
        subtraction = self.cpu - self.memory
        return f'cpu {self.__cpu} * {self.__memory} memory = {multiplication}\n' \
               f'cpu {self.__cpu} + {self.__memory} memory = {addition}\n' \
               f'cpu {self.__cpu} / {self.__memory} memory = {division}\n' \
               f'cpu {self.__cpu} - {self.__memory} memory = {subtraction}\n'

    def __str__(self):
        return f'cpu: {self.__cpu} memory: {self.__memory}'


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        self.sim_card_number = sim_card_number
        self.call_to_number = call_to_number
        return f'call to number {self.call_to_number} with sim card: {self.sim_card_number}'

    def __str__(self):
        return f'sim Cad list: {self.__sim_cards_list}'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        self.location = location

        return f'route laid {self.location}'


Comp = Computer(7, 9)
Phone_result = Phone({'Nurtelecom', 'Beeline'})
SmartPhone_result_1 = SmartPhone(9, 6, ('Nurtelecom', 'Beeline'))
SmartPhone_result_2 = SmartPhone(9, 6, ('Nurtelecom', 'Beeline'))
print(f'{Comp}\n{Phone_result}\n{SmartPhone_result_1}\n{SmartPhone_result_2}')

print(Comp.make_computations())
print(Phone_result.call(1, 555170707))
print(SmartPhone_result_2.use_gps('ХБК'))