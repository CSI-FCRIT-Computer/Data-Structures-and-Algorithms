# Arrays / List


# Creation

myArr = []
myArr2 = list()


# Inserting

myArr.append(1)
myArr.append(2)
myArr.append(3)
myArr.append(4)
myArr.append(5)


# traversal

# method 1
for i in range(len(myArr)):
    print(myArr[i])

# method 2
for item in myArr:
    print(item)


# searching

x=2

# method 1
for i in range(len(myArr)):
    if myArr[i]==x:
        print("Found")
else:
    print("Not Found")

# method 2
if x in myArr:
    print("Found")
else:
    print("Not Found")


# Deleting 

print(myArr)
myArr.pop() # Deletes an element from end of array
print(myArr)
