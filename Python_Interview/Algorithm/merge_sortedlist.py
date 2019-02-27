a = [1, 3, 6, 9]
b = [1, 2, 5, 8, 11, 13, 16]

def merge_sorted_list(a, b):

    c = []

    while a and b:
        if a[0] >= b[0]:
            c.append(b.pop(0))
        else:
            c.append(a.pop(0))
        
    while a:
        c.append(a.pop(0))
    while b:
        c.append(b.pop(0))
    return c

print(merge_sorted_list(a, b))