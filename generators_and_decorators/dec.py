
def logger(func):
    def wrapper(*args, **kwars):
        result = None
        try:
            result = func(*args, **kwars)
            with open('logs.txt', 'a') as f:
                f.write(f'|{func.__name__}|{args}, {kwars}|{result}|True|\n')
            return result
        except:
            with open('logs.txt', 'a') as f:
                f.write(f'|{func.__name__}|{args}, {kwars}|{result}|False|\n')
    return wrapper

@logger
def sum(a,b):
    return a+b
@logger
def divide(a,b):
    return a/b

print(divide(1,2))
print(sum(1,2))
print(divide(1,0))

# print(div)


    

# try:
#     divide(1,2)
# except:
#     pass
# divide(1,0)


# def divide(a, b):
#     try:
#         result = a/b
#         with open('logs.txt', 'a') as f:
#             f.write(f'divide function-da a={a}, b={b} olan halda error bas vermedi \n')
#         return result
#     except:
#         with open('logs.txt', 'a') as f:
#             f.write(f'divide function-da a={a}, b={b} olan halda error bas verdi \n') 