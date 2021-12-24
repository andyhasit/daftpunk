import os
import subprocess

with open("../lyrics.txt") as fp:
    lyrics = [line.strip() for line in fp.readlines()]

script_output = subprocess.check_output(
    "python daftpunk.py",
    shell=True
).split(os.linesep)


correct_up_to = 1
for i, lines in enumerate(zip(lyrics, script_output), 1):
    if lines[0] != lines[1]:
        print('Failed on line {0}: "{1}" <> "{2}"'.format(i, lines[0], lines[1]))
        break
    correct_up_to += 1

if correct_up_to >= len(lyrics):
    print("All correct!!!")
else:
    print("Correct up to line:", correct_up_to)
