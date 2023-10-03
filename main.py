class User:
    def __init__(self, name, age, skill, access):
        self.name = name
        self._age = age
        self.skill=skill
        self.access=access
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, val):
        self._age = val

c=User(name='Дмитрий', age=22, skill='middle', access='rwx')
print(c.skill)
