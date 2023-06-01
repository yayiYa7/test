# encoding:utf-8
import csv

with open('fyx_chinamoney.csv', 'r') as file:
    reader = csv.reader(file)
    list = list(reader)
size = 80
lists = [list[i:i+size] for i in range(0, len(list), size)]
for l in lists:
    print(l)
