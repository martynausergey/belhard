class human:

    def __init__(self, first_name: str, last_name: str, age: int, grades: int):
        self.grades = grades
        self.age = age
        self.last_name = last_name
        self.first_name = first_name
    def __str__(self):
        return f"human({self.first_name=}{self.last_name=}{self.age=})
    @property
    def grades(self):
        return round(sum(self.grades) / len(self._grades), 2)

    def __gt__(self, other):
        self_grades = round(sum(self.grades) / len(self._grades), 2)
        other_grades = round(sum(other_grades) / len(other._grades), 2)
        return self_grades > other_grades

    def __lt__(self, other):
        return self.__avarage(self) < self.__avarage(other)
    def __ge__(self, other):
        return self.__avarage(self) >= self.__avarage(other)
    def __le__(self, other):
        return self.__avarage(self) <= self.__avarage(other)
    def __eq__(self, other):
        return self.__avarage(self) == self.__avarage(other)
    def __ne__(self, other):
        return self.__avarage(self) != self.__avarage(other)

