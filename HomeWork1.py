class House:
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def print_info(self):
        print(f'Это  {self.name}, в нем {self.number_of_floors} этажей')

    def go_to(self,new_floor):
        if int(new_floor) > int(self.number_of_floors):
            print(f"В {self.name} нет такого этажа!")
        else:
            print(f"едем на {new_floor} этаж {self.name}")
            for i in range(int(new_floor)):
                print(i + 1)

house1 = House("ЖК Золотые Ключи", 15)
house2 = House("ЖК Татьянин Парк", 14)

house1.print_info()
house2.print_info()
new_floor = input("введите номер этажа: ")

house1.go_to(new_floor)