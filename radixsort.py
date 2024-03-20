def radixsort(array):
    maxVal = max(array)
    exp = 1

    while maxVal // exp > 0:
        bins = [[] for _ in range(10)]  # Create 10 buckets

        for num in array:
            digit = (num // exp) % 10  # Get the digit at the current position
            bins[digit].append(num)

        array.clear()  # Clear the original array

       
        for bucket in bins:
            for item in bucket:
                array.append(item) # Append elements from buckets back to the original array

        exp *= 10

    return array

# Test the radix sort function

mylist = [6,5,8,9,3,10,15,12,16]
print(mylist)
radixsort(mylist)
print(mylist)