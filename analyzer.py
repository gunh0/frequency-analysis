import operator
import string

text = open("./ciphertext.txt")
letters = string.ascii_lowercase
total_count = 0

fre_of_eng_letters = {
    "e": 12.7,
    "t": 9.1,
    "a": 8.2,
    "o": 7.5,
    "i": 7.0,
    "n": 6.7,
    "s": 6.3,
    "h": 6.1,
    "r": 6.0,
    "d": 4.3,
    "l": 4.0,
    "c": 2.8,
    "u": 2.8,
    "m": 2.4,
    "w": 2.3,
    "f": 2.2,
    "g": 2.0,
    "y": 2.0,
    "p": 1.9,
    "b": 1.5,
    "v": 1.0,
    "k": 0.08,
    "j": 0.02,
    "q": 0.01,
    "x": 0.01,
    "z": 0.01,
}

for i in text:
    text_lower = i.lower()
    text_nospace = text_lower.replace(" ", "")
    text_clean = text_nospace.strip(string.punctuation)

for a in letters:
    num = text_clean.count(a)
    total_count += num

print("Total letters:", total_count)

fre_of_cipher = {}
for i in range(len(letters)):
    num = text_clean.count(letters[i])
    print(letters[i], "%03d" % num, num / total_count * 100)
    # fre_of_cipher[letters[i]] = num / total_count * 100
    fre_of_cipher[letters[i]] = num

print("Freq. of cipher:", fre_of_cipher)
sorted_fre_of_cipher = dict(sorted(fre_of_cipher.items(), key=lambda item: item[1]))
print("Sorted res. of ciper:", sorted_fre_of_cipher)
sorted_fre_of_eng_letters = dict(
    sorted(fre_of_eng_letters.items(), key=lambda item: item[1])
)
print("Sorted res. of eng:", sorted_fre_of_eng_letters)

convert_dict = {}
list_of_ci_key = list(sorted_fre_of_cipher.keys())
list_of_eng_key = list(sorted_fre_of_eng_letters.keys())
for i in range(len(list_of_ci_key)):
    convert_dict[list_of_ci_key[i]] = list_of_eng_key[i]
print("Convert dict.:", convert_dict)

file = open("./ciphertext.txt", "r")
line = file.readline()
print(line)
decrypt_line = ""
for alpha in line:
    decrypt_line += list_of_eng_key[list_of_ci_key.index(alpha)]
print(decrypt_line)
