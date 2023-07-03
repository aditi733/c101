import random

def dice():
    response=input('do you want to roll a dice? y/n')
    while response=='n':
        response=input('do you want to roll a dice? y/n')
        if response=='y':
            break
    no=random.randint(1,6)
    if response=='y':
        print(no)
    end=input('press y to roll again and n to exit.')
    if end=='y':
        dice()
    else:
        end
dice()