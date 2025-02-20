txt = input("Input: ")
new_txt = ""

for c in txt:
    if c.lower() in ["a", "e", "i", "o", "u"]:
        continue
    else:
        new_txt += c

print(f"Output: {new_txt}")
