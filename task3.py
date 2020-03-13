myList = list(map(int, input('Введите список чисел через пробел: ').split()))
step = int(input(': '))
print('before ', myList)
if step < 0:
    popedItem = myList.pop(0)
    myList.append(popedItem)
elif step > 0:
    popedItem = myList.pop()
    myList.insert(0, popedItem)
print('after ', myList)