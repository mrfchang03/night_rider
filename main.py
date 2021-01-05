# main.py
# Night Rider
# Text-based adventure game.
import sys
import textwrap
import time

INTRODUCTION = """
WELCOME TO NIGHT RIDER

WE'VE STOLEN A CAR. WE NEED TO GET IT HOME.
THE CAR IS SPECIAL.

THAT'S WHY THE GOVERNMENT WANTS IT.

WE CAN'T LET THEM HAVE IT.

ONE GOAL: SURVIVAL... and THE CAR
REACH THE END BEFORE THE MAN GON GETCHU.
"""

def main():
    for char in textwrap.dedent(INTRODUCTION):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
time.sleep(1)


    # TODO : Display introduction
    print(INTRODCUTION)
    # MAIN LOOP
        # TODO: Present the user their choices
    # TODO: Change the environment based on user choice and RNG
    # TODO: Random event generator

if __name__ == "__main__":
    main()