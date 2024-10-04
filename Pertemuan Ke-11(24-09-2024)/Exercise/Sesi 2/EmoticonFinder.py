def find_emoticons(text):
  emoticons = []
  for i in range(len(text)):
    if text[i] == ':':
      if i + 1 < len(text):
        emoticon = text[i:i + 2]
        emoticons.append(emoticon)
  return emoticons
text = input()
emoticons = find_emoticons(text)
for emoticon in emoticons:
  print(emoticon)