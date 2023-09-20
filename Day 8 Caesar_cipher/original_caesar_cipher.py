alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount
#  and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:  # Only process letters in the alphabet
            position = alphabet.index(letter)
            # using modulo operation wrap around to the start of the alphabet.
            new_position = (position + shift_amount) % len(alphabet)
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter  # Keep the character unchanged if it's not in the alphabet
    print(f"The encoded text is {cipher_text}.")


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift_amount) % len(alphabet)  # subtract to reverse the position.
            new_letter = alphabet[new_position]
            plain_text += new_letter
        else:
            plain_text += letter  # Keep the character unchanged if it's not in the alphabet
    print(f"The decoded text is {plain_text}.")


# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
# Call the encrypt function with keyword arguments
# encrypt(plain_text=text, shift_amount=shift)
# decrypt(cipher_text=text, shift_amount=shift)

# Check user's choice and call the appropriate function
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
else:
    print("Invalid choice!")
