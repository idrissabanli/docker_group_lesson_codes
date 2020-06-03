# range(10) [1,2,3,4,5,6,7,8,9,10]

# def custom_range(last_arg):
#     i = 0
#     if i != last_arg:
#         i+=1
#         yield i
# a = custom_range(3)

# print(next(a))
# a = [1,2,3,4,5]
# print([i**2 for i in a])
def get(di):

    for i in di.keys():
        yield i

d = {
    '1': 1,
    '2': 2,
    '3': 3
}
a = get(d)
print(next(a))
