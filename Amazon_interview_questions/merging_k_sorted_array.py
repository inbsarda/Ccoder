def sortArray(arr1, arr2):
    if not arr1:
        return arr2

    arr3 = []
    j = 0
    k = 0
    n = len(arr1) + len(arr2)
    for i in range(0,n-1):
        if arr1[j] > arr2[k]:
            arr3.append(arr2[k])
            k = k+1
            if k == len(arr2):
                break
        else:
            arr3.append(arr1[j])
            j=j + 1
            if j == len(arr1):
                break

    while k < len(arr2):
        arr3.append(arr2[k])
        k = k+1

    while j < len(arr1):
        arr3.append(arr1[j])
        j = j+1

    return arr3



a = {1:[1,5,8,9,11], 2:[2,12,24,44], 3:[3,4,6,13,19]}
b = []
for i in range(1,4):
    b = sortArray(b,a[i])


print(b)

        
