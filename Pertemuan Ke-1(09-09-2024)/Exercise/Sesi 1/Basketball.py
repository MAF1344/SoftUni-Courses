fee = int(input())
sneakers = fee - (fee * (40/100))
outfit = sneakers - (sneakers * (20/100))
ball = (outfit / 4)
accessories = (ball / 5)

print(f"Total Cost : {fee + sneakers + outfit + ball + accessories}")
