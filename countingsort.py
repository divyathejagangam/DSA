def countingsort(array):
    max_array = max(array)
    count = [0]*(max_array+1)

    while len(array) > 0:
        num = array.pop()
        count[num] += 1

    for i in range(0,len(count)):
        while count[i] > 0:
            array.append(i)
            count[i] -= 1

    return array

mylist=[3,4,6,6,7,5,3,1]

countingsort(mylist)

print(mylist)
