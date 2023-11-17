from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def format_shift_alphabet(shift_amount):
    # Create the shifted list with adding of the remained letters after shifting at the end of the list
    shift_alphabet = []
    shift_alphabet += alphabet[shift_amount:len(alphabet)]
    shift_alphabet += alphabet[0:shift_amount]
    return shift_alphabet


def caesar(input_text, shift_amount, cipher_direction):
    # According to direction, set the static_list and shifted_list
    if cipher_direction == "encode":
        static_list = alphabet
        shifted_list = format_shift_alphabet(shift_amount)
    elif cipher_direction == "decode":
        static_list = format_shift_alphabet(shift_amount)
        shifted_list = alphabet
    else:
        print(f"Your option \"{cipher_direction}\" is not valid.")
        return

    # Format output_text using the index of the letters that are paired into static list and shifted list
    output_text = ""
    for char in input_text:
        if char not in alphabet:
            output_text += char  # keep the number/symbol/space when the text is encoded/decoded
        else:
            for letter_alphabet in static_list:
                if char == letter_alphabet:
                    position_letter = static_list.index(letter_alphabet)
                    output_text += shifted_list[position_letter]

    print("Here's the ",
          'encoded' if cipher_direction == 'encode' else 'decoded',
          "result: " + output_text)


print(logo)

run_cipher = 'yes'
while run_cipher == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:  # if the user enters a shift number greater than 26, get the remained amount
        shift %= 26

    caesar(input_text=text, shift_amount=shift, cipher_direction=direction)

    run_cipher = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

print("Goodbye!")
