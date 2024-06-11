class Building:
    def __init__(self, total):
        self.name = total

    def add_buildind(self, n):
        print(f" Построено {n}-ое здание!!!")

    def print_info(self):
        print(f" Поступило задание: необходимо построить {self.name} зданий!!!")


building_dict = {}   # - создание 40 объектов типа "Building" в виде словаря
for i in range(40):
    building_dict["D" + str(i+1)] = Building(i + 1)

Building(40).print_info()
print(input("нажмите любую клавишу, чтобы приступить к заданию: "))

for i in range(40):  # - печать построенных объектов
    building_dict["D" + str(i+1)].add_buildind(i+1)




