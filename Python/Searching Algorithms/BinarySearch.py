# Time Complexity --> O(log n)

def binarySearch(array, value) :
    start = 0
    end = len(array)-1
    mid = (start+ end) //2
    while array[mid] != value :
        if value < array[mid] :
            end = mid-1
        else :
            start = mid +1
        mid = (start + end) // 2
    return mid

custArray = [6,12,24,30,36 , 42,48, 54,60]
print(binarySearch(custArray, 42))