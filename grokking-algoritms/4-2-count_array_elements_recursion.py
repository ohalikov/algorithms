def count_array_elements(array):
    if array == []:
        return 0
    return 1 + count_array_elements(array[1:])

arr = [1,2,3,45,545,54,45,45,45,45,45]
print(count_array_elements(arr))