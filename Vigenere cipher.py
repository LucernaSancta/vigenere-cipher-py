# TODO: Add comments and documentation

from math import ceil

alphabet = input("Alphabet (default: ABCDEFGHIJKLMNOPQRSTUVWXYZ): ").upper()
key = input("Key: ").upper()
message = input("Message: ").upper()


if not alphabet:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


alphabet = list(dict.fromkeys(list(alphabet)).keys())
ini_alp = "".join(alphabet)


if key:
    key = list(dict.fromkeys(list(key)).keys())
    key.reverse()

    for char in key:
        index = alphabet.index(char)
        alphabet.pop(index)
        alphabet.insert(0, char)
    
    key.reverse()

cipher = []
for char in alphabet:
    index = alphabet.index(char)

    cipher.append(alphabet[index:] + alphabet[:index])


message = list(message)
key_m = ("".join(key)) * ceil(len(message)/len(key))
finale = ""


i = 0
while i < len(message):
    if message[i] == " ":
        char = " "
    elif message[i] == "\n":
        char = "\n"
    else:

        index1 = alphabet.index(message[i])
        index2 = alphabet.index(key_m[i])

        char = cipher[index1][index2]

    finale += char
    i += 1

print()
print("-- OUTPUT --")
print()

for row in cipher:
    for char in row:
        print(char, end="")
    print()

print()
print("".join(key))
print(ini_alp)
print()

print(finale)