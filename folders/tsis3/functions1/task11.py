def palindrome():
    word = input()
    for i in range(len(word)):
        if word[i] != word[-(i+1)]:
            return print("The word is not a palindrome")
    return print("The word is a palindrome")