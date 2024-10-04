deposit = float(input())
term = int(input())
interest = float(input()) / 100
amount = deposit + term * ((deposit * interest) / 12)
print(f"The Total Amount Is : {amount}")