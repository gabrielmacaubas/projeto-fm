import csv
from quick_sort import *
import sys

print(sys.setrecursionlimit(4000))

b = []

with open("./dadosjp.csv", 'r') as file:
    csvreader = csv.reader(file)
    primeiro = True

    for row in csvreader:
        if primeiro:
            primeiro = False

            continue

        a = row[0].split(";")

        b.append([a[0], (float(a[1]) + float(a[2]) + float(a[3]) + float(a[4]) + float(a[5])) / 5])

quick_sort(b, 0, len(b)-1)
#merge sort
#bubble sort
#selection sort
#insertion sort
