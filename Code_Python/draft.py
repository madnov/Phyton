import sys

command = sys.argv[1]


def path(way: str) -> int:
    if command == 'way':
        total = count = 0
        for x in way:
            if x == 'u':
                total += 1
            elif x == 'd':
                total -= 1
            if total == 0:
                count += 1
        return count
print(path())

if command == "way":
    way = sys.argv[2]
    path(way)
