import traceback
a = input('a-ni daxil edin: ')
b = input('b-ni daxil edin: ')

try:
    print('here334')
    assert b.isdigit() or a.isdigit()
except Exception as e:
    print(dir(e))
    print('here')
    print(type(e).__name__)
    print(traceback.format_exc())


# if not b.isdigit() or not a.isdigit():
#     raise ValueError('Daxil olunan ededler reqem olmalidir')

# try:
#     print(str(int(a)/int(b)) * 'salam')
# except ZeroDivisionError as zde:
#     print(zde)
#     print('ikinci 0 ola bilmez')
# except  ValueError as ve:
#     print(ve)
#     print('Yalniz eded daxil ede bilersizin!')
# except Exception as e:
#     print(e)