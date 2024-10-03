#Класс Куб

class Cube:

    def __init__(self, num, stepen):
        self.Num = num
        self.Stepen = stepen

    def rise(self):
        return self.Num ** self.Stepen

print('Ваше число в кубе')
n = int(input('Введите ваше число:'))
s = 3
NewNum = Cube(n, s)
print(NewNum.rise())