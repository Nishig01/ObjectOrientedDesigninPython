#Iterators = an object that returns elements one at a time
#             from a sequence ( or data stream)
#             and remembers its position bw cells.
#           A python obj is an iterator if it has:
#               __iter__() -> returns the iterator obj itself
#               __next__() -> returns the next item in the sequence
# (raises StopIteration when no more items)
import random
class Dice:
    def __init__(self, rolls):
        self.rolls = rolls
        self.count = 0

    def __iter__(self): #returns itself whenever we call the obj it implicity calls this method behind the scenes
        return self

    def __next__(self): #returns next item in the sequence
        if self.count < self.rolls:
            self.count +=1
            return random.randint(1,6)
        else:
            raise StopIteration

# dice = Dice(3)
# for roll in dice:
#     print(f"{roll} roll")

dice = [die for die in Dice(3)]
print(dice) #[2, 3, 4]

dice = Dice(4)

# Behind the scenes-->
# iterator = iter(dice)
# iterator1 = dice.__iter__()
#both above are same

# while True:
#     try:
#         roll = next(iterator)
#         roll1 = iterator.__next__()
#         print(roll)
#     except StopIteration:
#         break
