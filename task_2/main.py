# вариант 4
from random import randint,choice
numbers = [-15, -4, -2, -7, 0, 3, 5, 12, 9]
height = randint(4,8)
width =randint(4,8)
sum = 0
num=[]
for i in range(height):
    arg = []
    for j in range(width):
        even = choice(numbers)

        if even % 3 != 0:
            sum += even
        arg.append(even)
    num.append(arg)
    print(' '.join(map(str,num[i])))
print(f"Сумма всех чисел некратных 3 - {sum}") 
