# https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

from math import ceil

alphabet = input("Alphabet (default: ABCDEFGHIJKLMNOPQRSTUVWXYZ): ").upper() # Original alphabet, to be modifiedwith the keyword
key = input("Key: ").upper() # Keyword
message = input("Message: ").upper()


# Default alphabet
if not alphabet:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Transform str alphabet in list and save the original one in 'ini_alp'
alphabet = list(alphabet)
ini_alp = "".join(alphabet)


if key:
    key = list(key)
    key.reverse()

    # Shift the alphabet
    for char in key:
        index = alphabet.index(char)
        alphabet.pop(index)
        alphabet.insert(0, char)

    key.reverse()
else:
    raise KeyError('You must provide a key')

# Create the cipher by shifting the alphabet
cipher = []
for char in alphabet:
    index = alphabet.index(char)

    cipher.append(alphabet[index:] + alphabet[:index])


message = list(message)
key_m = ("".join(key)) * ceil(len(message)/len(key)) # Reapeted keyword
final = ""


# Enchript the message
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

    final += char
    i += 1


# Print output

print("\n-- OUTPUT --\n")

for row in cipher:
    for char in row:
        print(char, end="")
    print()

print()
print("".join(key))
print(ini_alp)
print()

print(final)