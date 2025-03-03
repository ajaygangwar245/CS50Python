import emoji

name = input("Input: ").strip()

print(emoji.emojize(name, language="alias"))
