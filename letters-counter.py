# --------------------------------------
# - Letters Counter (letters-counter.py)
# - Version 1
# --------------------------------------

def letters_frequency(input_string):
    clear_text = input_string.lower().replace(" ", "")
    frequency = {}
    for char in clear_text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

text = input("Enter a string: ")
frequency = letters_frequency(text)

for char in frequency:
    print(char,"->",frequency[char])