alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
extended_alphabet = alphabet + alphabet


# def encrypt(plain_text, shift_amount):
#     encrypt_msg = ""
#     for letter in plain_text:
#         if letter in alphabet:
#             letter_index = alphabet.index(letter)
#             encrypt_msg += extended_alphabet[letter_index + shift_amount]
#         else:
#             encrypt_msg += letter
#     print(encrypt_msg)
#
#
# def decrypt(encrypt_text, shift_amount):
#     decrypt_msg = ""
#     for letter in encrypt_text:
#         if letter in alphabet:
#             letter_index = alphabet.index(letter)
#             decrypt_msg += extended_alphabet[letter_index - shift_amount]
#         else:
#             decrypt_msg += letter
#     print(f"decrypt massage {decrypt_msg}")
#
#
# if direction == "encrypt":
#     encrypt(plain_text=text, shift_amount=shift)
# if direction == "decrypt":
#     decrypt(encrypt_text=text, shift_amount=shift)
#

def caesar(plain_text, shift_amount, user_direction):
    out_put_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = 0
            if user_direction == "encode":
                new_position = position + shift_amount
            elif user_direction == "decode":
                new_position = position - shift_amount
            else:
                print("Invalid Direction Try again")
            out_put_text += extended_alphabet[new_position]
        else:
            out_put_text += letter

    print(f"Massage : {out_put_text}")


caesar(plain_text=text, shift_amount=shift, user_direction=direction)
