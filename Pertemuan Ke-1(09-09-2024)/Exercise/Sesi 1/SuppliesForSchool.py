pens = int(input()) * 5.80
markers = int(input()) * 7.20
detergent = int(input()) * 1.20
discount = int(input()) / 100

total = pens + markers + detergent
print(total - (total * discount))