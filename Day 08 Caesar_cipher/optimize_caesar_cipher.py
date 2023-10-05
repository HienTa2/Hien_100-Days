from art import logo

print(logo)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_dict = {char: index for index, char in enumerate(alphabet)}


def caesar_cipher(input_text, shift_amount, operation):
    output_text = ""
    if operation == "decode":  # check for decode outside the for loop
        shift_amount = -shift_amount
    for char in input_text:
        if char in alphabet_dict:
            # using the modulo against the len of the alphabet
            new_position = (alphabet_dict[char] + shift_amount) % len(alphabet)
            output_text += alphabet[new_position]
        else:
            output_text += char  # Keep the character unchanged if it's not in the alphabet
    return output_text


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    # Keep asking for a valid direction until the user provides one
    while direction not in ["encode", "decode"]:
        print("Invalid choice! Please enter 'encode' or 'decode'.")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    result = caesar_cipher(text, shift, direction)
    print(f"The {direction}d text is {result}.")

    continue_response = input("Type 'yes' if you want to run again. Otherwise type 'no'.\n").lower()
    if continue_response == "no":
        should_continue = False
        print("Goodbye")

