def shift_encode(message, shift):
    encoded_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                encoded_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encoded_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encoded_message += encoded_char
        else:
            encoded_message += char
    return encoded_message


def shift_decode(encoded_message, shift):
    decoded_message = ""
    for char in encoded_message:
        if char.isalpha():
            if char.islower():
                decoded_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decoded_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decoded_message += decoded_char
        else:
            decoded_message += char
    return decoded_message


while True:
    print("1. Encoding the Message")
    print("2. Decoding the Message")
    print("3. Exit")

    choice = input("Please enter number (1-2-3): ")

    if choice == "1":
        message_to_encode = input("Please enter the message to be encoded: ")
        shift_amount = int(input("Please enter the number of swipes: "))
        encoded_result = shift_encode(message_to_encode, shift_amount)
        print("Encoded Message:", encoded_result)

    elif choice == "2":
        encoded_message_to_decode = input("Please enter the message to be decoded: ")
        shift_amount_to_decode = int(input("Please enter the number of swipes: "))
        decoded_result = shift_decode(encoded_message_to_decode, shift_amount_to_decode)
        print("Decoded Message:", decoded_result)

    elif choice == "3":
        print("Program has ended!")
        break

    else:
        print("Invalid option!Please choice 1, 2 or 3!")
