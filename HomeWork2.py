class House:
    def __init__(self, name, numberOfFloors):
        self.name = name
        self.numberOfFlors = numberOfFloors
    def print_info(self):
        print(f'В {self.name} было {self.numberOfFlors} этажей')
    def setNewNombersOfFlors(self, floors):
        self.numberOfFlors = int(self.numberOfFlors) + int(floors)
        print(f"Теперь в {self.name} стало {self.numberOfFlors} этажей")

H1 = House("ЖК 'EVER'", 14)

H1.print_info()

H1.setNewNombersOfFlors(input(f"Введите кол-во этажей, которые дополнительно построили в {H1.name} ",))

