def sum(array):
    if array == []:
        return 0
    
    return array[0] + sum(array[1:])

arr = [1,2,3,4,5,6]
print(sum(arr))

