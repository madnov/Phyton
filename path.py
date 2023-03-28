import sys


def path(way):
    total = count = 0
    for x in way:
        if x == 'u':
            total += 1
        elif x == 'd':
            total -= 1
        if total == 0 and x == 'u':
            count += 1
    return count


command = sys.argv[1]
if command == "way":
    way = sys.argv[2]
    path(way)
    print(path(way))

