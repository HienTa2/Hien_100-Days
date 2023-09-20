alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_dict = {char: index for index, char in enumerate(alphabet)}


def caesar_cipher(input_text, shift_amount, operation):
    output_text = ""
    if operation == "decode": # check for decode outside of the for loop
        shift_amount = -shift_amount
    for char in input_text:
        if char in alphabet_dict:
            new_position = (alphabet_dict[char] + shift_amount) % len(alphabet)
            output_text += alphabet[new_position]
        else:
            output_text += char  # Keep the character unchanged if it's not in the alphabet
    return output_text


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction in ["encode", "decode"]:
    result = caesar_cipher(text, shift, direction)
    print(f"The {direction}d text is {result}.")
else:
    print("Invalid choice!")
