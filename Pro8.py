def count_list(li, min, max):
    c = 0
    for x in li:
        if min <= x <= max:
            c += 1
    return c


l = [10, 20, 70, 40, 57, 62, 92, 30, 99]
print(f'The number of elements in a {l} within {40} and {100} is: {count_list(l, 40, 100)}')
