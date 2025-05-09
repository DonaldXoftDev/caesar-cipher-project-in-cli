from caesar_ascii import logo
alphabets = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']

def caesar(message, shift, encode_or_decode):
    """this prints either the encoded text or decoded text as specified
    from the  direction by the user."""
    if encode_or_decode == 'decode':
        shift *= - 1

    output_text = ''
    for letter in message:
        if letter.isalpha():
            new_shift_index = alphabets.index(letter) + shift
            new_shift_index %= len(alphabets)
            output_text += alphabets[new_shift_index]
        else:
            output_text += letter
    print(output_text.capitalize())


end = False
while not end:
    print(logo)
    direction = input('Type either "encode" to encrypt or "decode" to decrypt a message: ').lower().strip()
    text = input('Enter the message:\n ').lower().strip()
    shift_amount = int(input('Enter the shift number: '))

    caesar(text,shift_amount,direction)

    want_to_end = input('Do you want to end? type "y" or "n": ').lower().strip()
    if want_to_end == 'y':
        end = True


