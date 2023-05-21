import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

end_program = 'yes'


def caesar(text, shift, direction):
    if shift > 25:
        shift = shift % 26
    temporary_text = list(text)
    text = []
    if direction == 'decode':
        shift -= shift*2
    for letter in temporary_text:
        if letter in alphabet:

            letter = alphabet[alphabet.index(letter)+shift]
            text += letter
        else:
            text += letter

    text = ''.join(text)
    print(f"Here's the {direction}d result: {text}")
    end_program = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'")
    if end_program == 'yes':
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)


caesar(text, shift, direction)
