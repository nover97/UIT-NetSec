from collections import Counter

orgnText = ""


def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict


try:
    with open("ciphertext.txt") as f:
        orgnText = f.read()
except FileNotFoundError:
    print("File not found")

letterDict = char_frequency(orgnText.strip().replace(" ", ""))
tempList = sorted(letterDict.items(), key=lambda x: x[1], reverse=True)
freqDict = dict(tempList)
print(freqDict)
# print((i, counts[i]) for i in counts)
