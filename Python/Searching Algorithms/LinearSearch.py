def linearSearch(array , value) :
    for i in range(len(array)) :
        if array[i] == value :
            return i
    return -1

print(linearSearch([2,1,6,7,4,5,3,9,8], 9))