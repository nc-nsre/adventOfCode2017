import day_01.InverseCaptia as ic


with open('input_1.txt') as inputfile:
    for line in inputfile:
        print(ic.captia(line))
        print(ic.captia(line, len(line) / 2))
