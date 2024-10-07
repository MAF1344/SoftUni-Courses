from math import ceil

people = int(input())
capacity = int(input())

courses = people / capacity

print(ceil(courses))