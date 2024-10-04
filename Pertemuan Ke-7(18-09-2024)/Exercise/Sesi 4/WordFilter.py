# text = list(map(str, input().split()))
#
# for word in text:
#     if len(word) % 2 == 0:
#         print(word)

text = input().split()
print('\n'.join(word for word in text if len(word) % 2 == 0))