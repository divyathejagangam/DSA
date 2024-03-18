def partition(arr,low,high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        
        while i <= j and arr[j] >= pivot:
            j -= 1

        if i > j:
            break
            
        arr[i],arr[j] = arr[j],arr[i] #swap i and j 

    arr[low],arr[j] = arr[j],arr[low] # finding sorted position of pivot element
    return j # index of sorted element

def quicksort(arr,low,high):
    if low < high:
       j = partition(arr,low,high)
       quicksort(arr,low,j-1)
       quicksort(arr,j+1,high)
    return arr

mylist = [6,5,8,9,3,10,15,12,16]

print(quicksort(mylist,0,len(mylist) - 1))