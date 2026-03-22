#multithreading = used to perform multiple tasks concurrently (multitasking)
#                 good for i/o bound tasks like reading files or fetching data from API's
#                 threading. Thread(target= my_function)

import threading
import time
def walk_dog(doogo):
    time.sleep(8)
    print(f"You finish walking the dog {doogo}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail(name, last):
    time.sleep(4)
    print(f"You get the mail from {name} {last}")

# walk_dog()
# take_out_trash()
# get_mail()
# You finish walking the dog
#You take out the trash
# You get the mail

chore1 = threading.Thread(target = walk_dog, args=("Scooby",)) #without , interpreted as string and not tuple we send args with tuple
chore1.start()

chore2 =threading.Thread(target = take_out_trash)
chore2.start()


chore3= threading.Thread(target = get_mail, args=("Nishi", "Mali"))
chore3.start()
#You take out the trash
# You get the mail
# You finish walking the dog

print("All chores aren't complete!") #prints first
# making the whole program wait  to complete all the threads-->
chore1.join()
chore2.join()
chore3.join()
print("All chores complete!")