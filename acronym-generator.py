# --------------------------------------
# - Acronym Generator (acronym-generator.py)
# - Version 1
# --------------------------------------

print(" ===================== ")
print(" = Acronym Generator = ")
print(" ===================== ")

phrase = input("#~ Type a Phrase: ")
acronym = ""

for word in phrase.split():
    if len(word) > 3 :
        acronym += word[0].upper()
    else:
        acronym += ''

print(f"Acronym of {phrase} is {acronym}")

