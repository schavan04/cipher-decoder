with open(r"message.txt", "r") as file:
    message = file.read().lower()
    file.close()

alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(' ')
frequencies = []
for a in alphabet: frequencies.append(0)

msg = list(message)
msg_list = sorted(msg)
msg_chars = []
for i in range(len(msg_list)):
    if msg_list[i].isalpha():
        msg_chars.append(msg_list[i])

for char in msg_chars: 
    frequencies[alphabet.index(char)] += 1

alph_copy = alphabet

for i in range(1, len(frequencies)):
    key = frequencies[i]
    alph = alph_copy[i]
    j = i-1
    while j >= 0 and key < frequencies[j]:
        frequencies[j+1] = frequencies[j]
        alph_copy[j+1] = alph_copy[j]
        j -= 1
    frequencies[j+1] = key
    alph_copy[j+1] = alph

frequencies.reverse()
alph_copy.reverse()

most_frequent_letters = "e a r i o t n s l c u d p m h g b f y w k v x z j q".split(' ')

decoded_msg = []

for char in msg:
    if char.isalpha():
        j = alph_copy.index(char)
        decoded_msg.append(most_frequent_letters[j])

decoded_msg = ''.join(decoded_msg)

print(decoded_msg)
