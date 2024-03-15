def selection_sort(array):
    n = len(array)
    for i in range (n-1):
        min_index = i
        array[min_index] = array[i]
        for j in range(i+1,n):
            if array[j] < array[min_index]:
                array[j],array[min_index] = array[min_index],array[j]
            
    return array
array = [ 5, 6, 6, 7,1, 3, 3, 4,]
selection_sort(array)
print(array)

