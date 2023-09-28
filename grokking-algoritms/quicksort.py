def quicksort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i < pivot ]
    greater = [i for i in array[1:] if i > pivot ]

    return quicksort(less) + [pivot] + quicksort(greater)


arr = [10,5,2,3]
sorted_array = quicksort(arr)
print(sorted_array)


# function quicksort2 (array) {
#     const arr = [...array]
#     const newArr = []
#     if (arr.length < 2) return arr;
#     let pivot = arr[0];
#     let less = arr.filter(el => el < pivot);
#     let greater = arr.filter(el => el > pivot);
#     newArr.push(quicksort2(less))
#     newArr.push(pivot)
#     newArr.push(quicksort2(greater))
#     return newArr
# }