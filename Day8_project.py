alphabet =  [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]
# my rough idea
# message = "hello"
# encode = ""
# shift = 1
#
# for letter in message:
#     encode += alphabet[alphabet.index(letter) + shift]
# print(encode)

# 100 days of code
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    encoded_msg = ""
    for letter in original_text:
        shifted_index = alphabet.index(letter) + shift_amount
        shifted_index %= len(alphabet)
        encoded_msg += alphabet[shifted_index]
    print(f"Here is the encoded result: {encoded_msg}")

def decrypt(encoded_text, shift_amount):
    decoded_msg = ""
    for letter in encoded_text:
        shifted_index = alphabet.index(letter) - shift_amount
        shifted_index %= len(alphabet)
        decoded_msg += alphabet[shifted_index]
    print(f"Here is the decoded result: {decoded_msg}")

def ceaser():
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Invalid option")

main()