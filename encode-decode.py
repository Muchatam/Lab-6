# Micah Tam

def main():
    while True:
        print('''Menu
-------------
1. Encode
2. Decode
3. Quit
''')
        choice = int(input('Please enter an option: '))
        if choice == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!')
        elif choice == 2:
            decoded_password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.')
        elif choice == 3:
            break


def encode(password):
    list_pass = [*password]
    for i in range(len(list_pass)):
        list_pass[i] = int(list_pass[i]) + 3
        if list_pass[i] >= 10:
            list_pass[i] -= 10
    str_list = [str(i) for i in list_pass]
    encoded_pass = ''.join(str_list)
    return encoded_pass


def decode(encoded_password):
    tempValue = list(encoded_password)
    newList = []
    for j in tempValue:
        j = int(j)
        j -= 3
        if j == -2:
            j = 8
        if j == -1:
            j = 9
        newList.append(j)
    newList = [str(k) for k in newList]
    finalVal = ''.join(newList)
    return finalVal

if __name__ == '__main__':
    main()