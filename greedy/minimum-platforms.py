import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


def find_min_platforms(arrival, departure):
    arrival.sort()
    departure.sort()

    i = 0 # Arrival pointer
    j = 0 # Departure pointer
    count = 0
    platforms = 0

    while i < len(arrival):
        if arrival[i] < departure[j]:
            count += 1
            platforms = max(platforms, count)
            i += 1
        else:
            count -= 1
            j += 1

    return platforms

arrival = [2.00, 2.10, 3.00, 3.20, 3.50, 5.00]
departure = [2.30, 3.40, 3.20, 4.30, 4.00, 5.20]

print('Minimum platforms needed: ', find_min_platforms(arrival, departure))
