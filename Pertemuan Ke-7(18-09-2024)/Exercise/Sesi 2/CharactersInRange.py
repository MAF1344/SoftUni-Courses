char1 = input()
char2 = input()

char1 = ord(char1)
char2 = ord(char2)

def charRange(a, b):
    for i in range(a + 1, b):
        print(chr(i), end=' ')

charRange(char1, char2)