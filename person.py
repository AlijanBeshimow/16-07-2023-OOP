# class Person:
#     def __init__(self, name="Alex", age="32", type="Men"):
#         self.name = name
#         self.age = age
#         self.type = type

#     def __str__(self) -> str:
#         return f"{self.name}\t{self.age}-{self.type}"


# class Baby(Person):
#     def __init__(self):
#         super().__init__()
#         self.date_birth = "date_birth"


# ec = Baby()
# print("Men", ec.age)
# ec.age = "12"
# print("Baby", ec.age)


class Animal:
    def __init__(self, legs=4, name="Animal", eyes=2):
        self.legs = legs
        self.eyes = eyes
        self.name = name

    def walk(self):
        print(self.name, "Walking on 4 legs...")

    def __str__(self) -> str:
        return f"{self.name}\t{self.legs}"


class Spider(Animal):
    def __init__(self, name="Spider"):
        super().__init__()
        self.legs = 6
        self.color = "Black"
        self.name = name

    def walk(self):
        print("Spider is crawling...")

# black_widow = Spider()
# tarantula = Spider()
# print(black_widow)
# print(tarantula)


elephant = Animal()
spider = Spider()
# elephant.walk()
# spider.walk()


for animal in [elephant, spider]:
    animal.walk()
