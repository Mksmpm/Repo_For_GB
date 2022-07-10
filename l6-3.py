class Worker:
    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'salay': salary, 'bonus': bonus}


class Position(Worker):
    def get_name(self):
        return f"{self.name} {self.surname}"

    def get_income(self):
        return f"{sum(self._income.values())}"


worker = Position("Vova", "Crust", "Administrator", 40000, 6000)
print(worker.get_name())
print(worker.position)
print(worker.get_income())
