class House:
    def __init__(self, name, number_or_floors):
        self.name = name
        self.number_or_floors = number_or_floors


    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_or_floors:
            print('Такого этажа не существует')
        else:
            for new_floor in range(1, new_floor + 1):
                print(new_floor)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)