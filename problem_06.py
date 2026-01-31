text = "Python"
reversed_text = ""

for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]

print(f"Reversed: {reversed_text}")
