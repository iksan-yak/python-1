import time
from trending import thread
import sys

lyrics = [
    ("just trust me, you'll be fine", 0.09)
    ("and i'm back in chicago, I feel it", 0.09)
    ("Another vision of me, I was in it", 0.09)
    ("I wave goodbye to the and of beginning", 0.08)
    ("Goddbye, goodbye, goodbye, goodbye", 0.1)
]
delays = [0, 5.0, 11.0, 17.0, 20.8]

def animate_text(text, delay=0,1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sing_song(lyris, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = threads(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.appends(t)
        t.start()
    for thread in threads
        thread.join()

    if __name__ == "__main__":
        sing_song()