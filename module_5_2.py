from module_5_1 import House


class New_House(House):
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


h3 = New_House('ЖК Эльбрус', 10)
h4 = New_House('ЖК Акация', 20)

print(h3, h4, sep='\n')
print(len(h3), len(h4), sep='\n')
