# Работа не волк

class Programmer:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.money = 0
        self.worked = 0
        self.upper_senior = 0
    
    def work(self, time):
        self.worked += time
        if self.position == "Junior":
            self.money += time * 10
        elif self.position == "Middle":
            self.money += time * 15
        elif self.position == "Senior" and self.upper_senior == 0:
            self.money += time * 20
        else:
            self.money += (time * 20) + (self.upper_senior * time)
    
    def rise(self):
        if self.position == "Junior":
            self.position = "Middle"
        elif self.position == "Middle":
            self.position = "Senior"
        else:
            self.upper_senior += 1
    
    def info(self):
        return f"{self.name} {self.worked}ч. {self.money}тгр."


programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
