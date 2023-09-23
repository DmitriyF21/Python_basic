class Cat():
    def __init__(self,breed,color,age):
        self.breed=breed
        self.color=color
        self.age=age

    def meow(self):
        print('Мяу')

    def purr(self):
        print('Мрр')
cat1=Cat('Шотландская','Серая','3')

cat1.breed='Сиамская'
print(cat1.breed)