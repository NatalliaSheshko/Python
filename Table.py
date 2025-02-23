class Table:
    __mass = 0

    def __init__(self, mass0):
        self.__mass = mass0

    # чтение инкапсулированной массы
    def get_mass(self):
        return self.__mass

#журнальный стол
class JournalTable(Table):
    storage = 0


# обеденный стол
class DinnerTable(Table):
    __places = 0

    def __init__(self, mass0):
        Table.__init__(self, mass0)
        self.__places = mass0//5

    # чтение инкапсулированного числа мест
    def get_places(self):
        return self.__places


class Truck:
    __maxMass = 0
    __tables = []
    __count_table = 0

    def __init__(self, max_mass):
        self.__maxMass = max_mass

    def add(self, table):
        if self.__maxMass>self.count():
            self.__tables.append(table)
            self.__count_table +=table.get_mass()
            print("Загружен 1 стол класса ", table.__class__.__name__)
        else:
            print("Максимальная масса грузоподъемности достигнута")

    def count(self):
        return self.__count_table


table1 = Table(1)
table2 = JournalTable(2)
table3 = DinnerTable(3)

truck1 = Truck(2)
truck1.add(table1)
truck1.add(table2)
truck1.add(table3)
