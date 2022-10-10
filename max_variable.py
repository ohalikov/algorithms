def max_variable(array):
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    sub_max = max_variable(array[1:]) 
    return array[0] if array[0] > sub_max else sub_max

array = [1,5,3,2,6,3,2]

print(max_variable(array))

