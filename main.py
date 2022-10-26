def encode(num):
    result = 0
    for i in range(0, 8):
        digit = num // (10 ** i) % 10
        digit += 3 if (digit + 3 < 10) else -6
        result += digit * (10 ** i)
    return result


if __name__ == '__main__':
    encoded_num = -1

    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        user_opt = input('Please enter an option: ')
        if user_opt == '1':
            try:
                encoded_num = encode(int(input('Please enter your password to encode: ')))
                print('Your password has been encoded and stored!\n')
            except ValueError:
                print('Error: Incorrect input. Please try again.\n')
        elif user_opt == '2':
            pass
        elif user_opt == '3':
            print('Thanks for using this program.')
            break
        else:
            print('Error: Incorrect input. Please try again.\n')
