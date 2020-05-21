# def sum(*args):
#     s = 0
#     print(args)
#     for i in args:
#         s+=i
#     return s



def sum(a,b, *args, **kwargs):
    print('args', args)
    print('kwargs', kwargs)
    print(f"a={a} b={b}")
    return a + b
    

print(sum(1,5,6,7,3,5,7,9))
print(sum(3,5))
print(sum(a=1,b=3, c=4))

[1,2,3,4]