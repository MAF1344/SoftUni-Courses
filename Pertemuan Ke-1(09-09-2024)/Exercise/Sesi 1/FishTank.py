length = int(input())
width = int(input())
height = int(input())
percentage = float(input()) / 100
volume = (length * width * height) / 1000

print(f"{volume * (1 - percentage)}")
