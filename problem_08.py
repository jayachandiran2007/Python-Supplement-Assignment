def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

word = "Racecar"
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
