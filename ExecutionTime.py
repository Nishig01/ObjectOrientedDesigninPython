import time

# start_time = time.perf_counter()

# your code goes here
# for i in range(1000000000):
#     pass
#
# end_time = time.perf_counter()
#
# elapsed_time = end_time -start_time
#
# print(f"Elapsed time: {elapsed_time:.1f} seconds")

# /////////// Python dates n times
import datetime

# date = datetime.date(2025, 1,2)
# today = datetime.date.today()

# time = datetime.time(12, 30, 0)

# now = datetime.datetime.now() #within the date time module there's date time class we access

# now = now.strftime("%H:%M:%S %m-%d-%Y")

# print(date, today, time, now)
# print(now)
#
# target_datetime = datetime.datetime(2020,1,2, 12,30,1)
#
# current_datetime = datetime.datetime.now()
#
# if target_datetime < current_datetime:
#     print("target date has passed")
# else:
#     print("target date has NOT passed")

# Code an alarm clock using python
import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"{alarm_time} is set to alarm")
    sound_file = "my_music.mp3" #haven't downloaded
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            # pygame.mixer.music.play()

            # while pygame.mixer.music.get_busy():
            #     time.sleep(1)

        is_running = False
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Please enter the alarm time: (HH:MM:SS): ")
    set_alarm(alarm_time)
    # download song sudio from youtube audios
