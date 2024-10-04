def decipher_this():
    text = input()
    words = text.split()
    deciphered = []
    for word in words:
        char_code = ''.join([ch for ch in word if ch.isdigit()])
        first_char = chr(int(char_code))
        rest_of_word = word[len(char_code):]
        if len(rest_of_word) > 1:
            rest_of_word = rest_of_word[-1] + rest_of_word[1:-1] + rest_of_word[0]
        deciphered.append(first_char + rest_of_word)
    print(' '.join(deciphered))

decipher_this()