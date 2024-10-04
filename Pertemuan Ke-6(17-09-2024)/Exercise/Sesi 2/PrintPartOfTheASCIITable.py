char1 = int(input())
char2 = int(input())


for i in range(char1, char2 + 1):
    print(chr(char1), end=' ')
    char1 += 1