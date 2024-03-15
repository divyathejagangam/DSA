def insertion_sort(array):
    n = len(array)
    for i in range (1,n):
        insert_index = i
        current_value = array[i]
        for j in range (i-1,-1,-1):
            if array[j] > array[i]:
                array[j+1] = array[j]
                insert_index = j
            else:
                break
        array[insert_index] = current_value
    return array

mylist=[3,4,6,6,7,5,3,1]

insertion_sort(mylist)

print(mylist)
