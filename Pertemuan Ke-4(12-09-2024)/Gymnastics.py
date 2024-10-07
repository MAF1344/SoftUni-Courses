country = input()
apparatus = input()
difficulty = 0
performance = 0

if country == 'Russia':
    if apparatus == 'ribbon':
        difficulty += 9.100
        performance += 9.400
    elif apparatus == 'hoop':
        difficulty += 9.300
        performance += 9.800
    elif apparatus == 'rope':
        difficulty += 9.600
        performance += 9.000
    else:
        print('Error')
elif country == 'Bulgaria':
    if apparatus == 'ribbon':
        difficulty += 9.600
        performance += 9.400
    elif apparatus == 'hoop':
        difficulty += 9.550
        performance += 9.750
    elif apparatus == 'rope':
        difficulty += 9.500
        performance += 9.400
    else:
        print('Error')
elif country == 'Italy':
    if apparatus == 'ribbon':
        difficulty += 9.200
        performance += 9.500
    elif apparatus == 'hoop':
        difficulty += 9.450
        performance += 9.350
    elif apparatus == 'rope':
        difficulty += 9.700
        performance += 9.150
    else:
        print('Error')
else:
    print('Error')

print(f"The team of {country} get {difficulty + performance:.3f} on {apparatus}.")
print(f"{(20 - (difficulty + performance)) / 20 * 100:.2f}%")