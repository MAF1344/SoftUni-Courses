first_words = input()
second_words = input()

previous_words = first_words

for i in range(len(second_words)):
    new_words = second_words[:i + 1] + first_words[i + 1:]

    if new_words != previous_words:
        print(new_words)

    previous_words = new_words
