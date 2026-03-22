import random

# random.random()#generates random values between 0 to 1
# for i in range(3):
#     # print(random.random())
#     print(random.randint(1, 100))

# members = ['john', 'mary', 'terra', 'pony']
# print(random.choice(members))

# Dice
class Dice:
    def roll_dice(self):
        first= random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second # automatically interpreted as tuple
