import time;
from playsound import playsound;

length = int(input("How long should the timer be? (s)"));

def timer(length):
    while length > 0:
        min = int(length/60)
        sec = length % 60
        print(f'{min}m:{sec}s');
        length = length - 1;
    print("Time's up!");
    playsound("./mixkit-sound.wav");
timer(length);

