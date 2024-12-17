def isPalindrome(word):
    word = word.replace(" ", "").lower() # remove spaces and make it lowercase
    return word == word[::-1]

word = isPalindrome("malayalam")
print(word)
