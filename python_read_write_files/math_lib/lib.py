def int_input(msg):
    value = input(msg)
    if not value.isdigit():
        print('Yalniz eded daxil ede bilersiniz! ')
        exit()
    return int(value)


if __name__ == '__main__':
    a = int_input('a-ni daxil edin: ')
    b = int_input('b-ni daxil edin: ')
    print('a+b =', a+b )
