camelcase = input("camelCase: ")
result = ""
for character in camelcase:
    if character.isupper():
        result += "_" + character.lower()
    else:
        result += character
print(result)
