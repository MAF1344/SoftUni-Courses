bitcoin = int(input()) * 1168
yuan = float(input()) * 0.15 * 1.76
commission = float(input()) / 100

total = ((bitcoin + yuan) / 1.95) - (((bitcoin + yuan) / 1.95) * commission)
print(f"{total:.2f}")