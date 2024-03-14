def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        swap_flag = False
        for j in range(n-1-i):
            if (array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1] , array[j]
                swap_flag = True
        if not swap_flag:
            break
    return array

mylist=[3,4,6,6,7,5,3,1]

bubble_sort(mylist)
print(mylist)