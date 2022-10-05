def findKey(words: list) -> int:
    new = sorted(words, key=lambda el: len(el))
    if len(new[0]) == 1 and new[0].isalpha():
        if new[0].isupper():
            return ord(new[0]) - 65
        else:
            key = ord(new[0]) - 97
    else:
        key = -30
    return key


def decryptALetter(charr: str) -> str:
    if charr.isalpha():
        if charr.isupper():
            return chr((ord(charr) - 65 - key) % 26 + 65)
        else:
            return chr((ord(charr) - 97 - key) % 26 + 97)
    else:
        return charr


# key = int(input("Insert key: "))
# orgnText = input("Insert text: ")
orgnText = ""

try:
    with open("ciphertext_caesar.txt") as f:
        orgnText = f.read()
except FileNotFoundError:
    print("File not found")

words = orgnText.split()
result = ""
key = findKey(words)
if key != -30:
    print("Key is: ", key)
    joined = " ".join(words)
    for i in range(len(joined)):
        result = result + (decryptALetter(joined[i]))
    print(result)
