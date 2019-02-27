def quick_sort(l):
    if len(l) < 2:
        return l
    else:
        pivot = l[0]
        less = [i for i in l[1:] if i <= pivot]
        bigger = [i for i in l[1:] if i > pivot]
        result = quick_sort(less) + [pivot] + quick_sort(bigger)
        return result
print(quick_sort([1, 5, 2, 100, 23, 8, 12 , 323, 809, 11, 1]))