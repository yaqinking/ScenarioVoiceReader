# Use pyttsx3 generate scenario voice file.
# https://pyttsx3.readthedocs.io/en/latest/engine.html#examples

import pyttsx3
# Scenario text file to process
scenario = 'test.txt'

file = open(scenario, mode='r', encoding='utf8')
lines = file.readlines()

engine = pyttsx3.init()

output = ''
for line in lines:
    # engine.say(line)
    output += line

# Save .txt to .wav voice file
engine.save_to_file(output, '{0}.wav'.format(file.name))
engine.runAndWait()

print("End")
