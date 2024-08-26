"""
Задача "Мифическое наследование"
Цель: закрепить знания множественного наследования в Python.
"""
class Horse:                          # Базовый класс 1
    x_distance = 0                    # атрибут класса  -  пройденный путь
    sound = 'Frrr'
    def run(self, dx):           # dx - увеличивает x_distance на dx
        self.dx = dx
        self.x_distance = self.x_distance + dx
        return self.x_distance


class Eagle:                        # Базовый класс 2
    y_distance = 0                  # атрибут класса  -  высота полёта
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):              # dy - увеличивает y_distance на dy
        self.dy = dy
        self.y_distance = self.y_distance + dy
        return self.y_distance


class Pegasus(Horse, Eagle):                     # Дочерний класс
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        Horse.run(self, dx)
        Eagle.fly(self, dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(Eagle.sound)




p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

