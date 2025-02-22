import random  
 
def creatArray():
    r = 0
    print('Input first index matrix: ')
    x = int(input())
    print('Input second index matrix: ')
    y = int(input())
    array = []
 
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(random.randint(0,100))
            r += 1  
 
    return array
 
print(creatArray())
