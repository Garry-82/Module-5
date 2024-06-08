class Building:
    def __init__(self, _name_, numberOfFloors, buildingType):
        self._name_ = _name_
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType
    def __eq__(self, other):
        if self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType:
            return print(f"здание {self._name_} и здание {other._name_} одинаковы !!!!")
        else:
            return print(f"здание {self._name_} отличается от здания {other._name_}.....")

B1 = Building("Федерация", 65, "монолит")
B2 = Building("Меркурий",54,"стекло")
B3 = Building("Империя", 48, "монолит")
B4 = Building("ОКО", 65, "монолит")

B1 == B2
B2 == B3
B4 == B1