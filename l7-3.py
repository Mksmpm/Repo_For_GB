class Cell:

    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity < other.quantity:
            raise ValueError(
                "You cannot subtract when the number of sub-cells in the second cell is greater than the first one")
        return Cell(self.quantity - other.quantity)

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(self.quantity // other.quantity)

    def __str__(self):
        return f"{self.quantity}"

    def make_order(self, row_length):
        return '\n'.join(['*' * row_length for _ in range(self.quantity // row_length)]) + '\n' + '*' * (
                self.quantity % row_length)


cell1 = Cell(29)
cell2 = Cell(15)

print(cell1 + cell2)
print(cell1 * cell2)
print(cell1 - cell2)
print(cell1 / cell2)

print(Cell.make_order(cell1, 9))
