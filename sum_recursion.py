def sum(array):    
    x = array[len(array)-1]
    if len(array) == 1:
        return x
    else:
        return x + sum(array[:-1])
    
arr = [5,1,10,1,5]

print(sum(arr))
# print(len(arr))


# ex 2


def sum_2(array):
    if array == []:
        return 0
    else:
        return array[0] + sum_2(array[1:])
    
    
print(sum_2(arr))