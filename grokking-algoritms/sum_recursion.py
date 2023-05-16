def sum(array):
    if not array:
        return 0
    
    array_copy = array.copy()
    total = array_copy.pop()
    
    return total + sum(array_copy)


array = [1,2,3,4]
array3 = [7]
array2 = []
print(sum(array2))
print(sum(array))
print(sum(array3))
print(array)
print(array2)
print(array3)