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

    def __len__(self):
        return self.number_or_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_or_floors}"

    def __eq__(self,other):
        return self.number_or_floors == other.number_or_floors

    def __lt__(self,other):
        return self.number_or_floors < other.number_or_floors

    def __le__(self,other):
        return self.number_or_floors <= other.number_or_floors

    def __gt__(self,other):
        return self.number_or_floors > other.number_or_floors

    def __ge__(self,other):
        return self.number_or_floors >= other.number_or_floors

    def __ne__(self,other):
        return self.number_or_floors != other.number_or_floors

    def __add__(self,value):
        self.number_or_floors += value
        return self

    def __radd__(self,value):
        self.number_or_floors += value
        return self

    def __iadd__(self,value):
        self.number_or_floors += value
        return self

    houses_history = []

    def __new__(cls, *args, **kwargs):
        instance = super(House, cls).__new__(cls)
        house_name = args[0]
        cls.houses_history.append(house_name)
        return instance

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")