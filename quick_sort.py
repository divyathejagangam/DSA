
def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        items_lower = []
        items_greater = []
        pivot = sequence.pop()
        for item in sequence:
            if item < pivot:
                items_lower.append(item)
            else:
                items_greater.append(item)
        return (quick_sort(items_lower) + [pivot] + quick_sort(items_greater))
mylist = [55,55,2,3,7,0]
print(quick_sort(mylist))





