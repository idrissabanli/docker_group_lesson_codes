def int_input(msg):
    value = input(msg) # "5"
    if value.isdigit():
        value_int = int(value)
    else:
        print('yalniz reqem daxil ede bilersiniz')
        exit()
    return value_int # 5

a = int_input("A deyisenini daxil edin: ") # 5
b = int_input("B deyisenini daxil edin: ") # 6

summary = a + b

print(f"summary {summary}")