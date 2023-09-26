class TooYoungUser(Exception):
    pass
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

    # @staticmethod
    # def _age_validator(self,age):
    #     self.age = int(age)
    #     if self.age < 21:
    #         raise TooYoungUser('To young', age)
    #     return age

c=User (name='Дмитрий', age=20, skill='middle', access='rwx')
print(c.age)

try:
