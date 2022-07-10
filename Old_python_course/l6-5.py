class Stationery:
    def __init__(self, title='Paper'):
        self.title = title

    def draw(self):
        print(f"Drawing on {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Drawing with a pen on {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Drawing with a pencil on {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Drawing with a marker on {self.title}")


st_obj = Stationery()
st_obj.draw()

Handle().draw()
Pen().draw()
Pencil().draw()
