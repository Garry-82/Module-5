class Building:

    total = 0  # счетчик экземпляров класса Building
    def __init__(self):
        Building.total += 1
    def print_info(self,name):
        self.name = "B" + str(name)
        print(f" Создан {Building.total}-ый экземпляр класса Building с именем {self.name}!!!")

print(input("нажмите любую клавишу, чтобы приступить к заданию: "))

building_dict = {}   # - словарь объектов класса Building

for i in range(40):
    building_dict["B" + str(i+1)] = Building().print_info(Building.total)









