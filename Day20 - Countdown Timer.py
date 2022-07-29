#!/usr/bin/env python3.10

import time


def countdown(time_in_seconds: int) -> None:
    """prints a live countdown timer to screen

    Args:
        time_in_seconds (int): time to start the countdown(sec)
    """
    while time_in_seconds != 0:
        mins, secs = divmod(time_in_seconds, 60)
        time_remaining = "{:02d}:{:02d}".format(mins, secs)
        print(chr(10140), " ", end="")
        print(time_remaining, end="\r")
        time.sleep(1)
        time_in_seconds -= 1
    print("Time Elapsed", chr(9200))


print()
print(" COUNTDOWN TIMER ".center(30, "-"), end="\n\n")
time_in_seconds = int(
    input("Input time in seconds: "))
countdown(time_in_seconds)
