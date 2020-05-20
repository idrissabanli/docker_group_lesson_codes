a = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
searched_num = 9

mid_index = len(a)//2
min_index = 0
max_index = len(a)

while searched_num != a[mid_index]:
    if searched_num >= a[mid_index]:
        min_index = mid_index
        mid_index = (max_index + mid_index)//2
    else:
        max_index = mid_index
        mid_index = (min_index + mid_index)//2
    if not a[min_index] <= searched_num <= a[max_index-1]:
        print('element movcud deyil')
        break

print(mid_index)