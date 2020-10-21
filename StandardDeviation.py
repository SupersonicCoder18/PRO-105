import math
import csv

with open("PRO 105.csv", newline = "") as f:
    reader = csv.reader(f)
    filedata = list(reader)

data = filedata[0]

def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total+=int(x)
    mean = total/n
    return mean

SquaredList = []

for number in data:
    a = int(number)-mean(data)
    a = a**2
    SquaredList.append(a)

sum = 0

for i in SquaredList:
    sum = sum+i

result = sum/(len(data)-1)
StandardDeviation = math.sqrt(result)
print(StandardDeviation)