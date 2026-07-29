#printing ceaser art
import art
print(art.logo)

#here is the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def ceaser(original_text, shift_amount, encode_or_decode):
    ceaser_text = []
    for char in original_text:
        if char in alphabet:
            if encode_or_decode == 'encode':
                new_position = (alphabet.index(char) + shift_amount) % len(alphabet)
            elif encode_or_decode == 'decode':
                new_position = (alphabet.index(char) - shift_amount) % len(alphabet)
            ceaser_text.append(alphabet[new_position])
        elif char not in alphabet:
            ceaser_text.append(char)
    new_ceaser_text = "".join(ceaser_text)
    print(f"your {direction} message is: {new_ceaser_text}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    ceaser(original_text= text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' or 'no' to continue:\n").lower()
    if restart == 'no':
        print(f"Goodbye!")
        break
    else:
        continue