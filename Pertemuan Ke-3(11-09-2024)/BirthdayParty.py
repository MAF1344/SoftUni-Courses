rent = float(input())

cakes = rent * 20/100
drinks = cakes - (cakes * 45/100)
entertainer = rent / 3

cost = (rent + cakes + drinks + entertainer)

print(f"{cost:.1f}")
