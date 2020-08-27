
import random
a = [1,2,3,4,5]
def game():
    b = 0
    while b!=3:
        b = b+1
        choose = int(input('Число:'))
        if random.choice(a) == choose:
            print("you win")
        else:
            print("you lose")
game()