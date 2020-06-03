# range(10) [1,2,3,4,5,6,7,8,9,10]
def behave_like_range(f):
    def wrap(*args, **kwargs):
        print(args)
        if len(args)==1 and not 'first_index' in kwargs:
            return f(0, *args, **kwargs)
        else:
            print('here')
            return f(*args, **kwargs)
    return wrap


@behave_like_range
def custom_range(first_index, last_index, step=1):
    i = first_index
    while i < last_index:
        yield i
        i+=step

a = custom_range(3)



for i in a:
    print(i)

b = custom_range(1, 3)

print('b elements')
for i in b:
    print(i)

c = custom_range(0, 3, 2)

print('c elements')
for i in c:
    print(i)

d = custom_range(first_index=20, last_index=30, step=2)

print('d elements')
for i in d:
    print(i)

range(10)
def range(first_index, last_index , step=1):
    return a+b+c
range(first_index=1, 20, 2)