def palindrome(word, index=0):
    # Base case: if the index reaches the middle of the word
    if index >= len(word) // 2:
        return f"{word} is a palindrome"

    # Compare characters from both ends
    if word[index] != word[len(word) - index - 1]:
        return f"{word} is not a palindrome"

    # Recursive call with the next index
    return palindrome(word, index + 1)


# Example usage
print(palindrome("abcba", 0))
print(palindrome("peter", 0))
