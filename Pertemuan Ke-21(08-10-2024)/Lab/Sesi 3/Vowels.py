class vowels:
    def __init__(self, string):
        self.string = string
        self.index = 0
        self.vowels = "AEIOUaeiou"

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.string):
            char = self.string[self.index]
            self.index += 1
            if char in self.vowels:
                return char
        raise StopIteration

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

