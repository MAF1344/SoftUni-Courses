string1 = input().split(', ')
string2 = input().split(', ')

new_string = [word1 for word1 in string1 if any(word1 in word2 for word2 in string2)]

print(new_string)   