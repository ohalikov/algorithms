def find_smallest_element(arr):
    smallest = arr[0]
    smallest_index = 0

    for index, item in enumerate(arr):
        if smallest > item:
            smallest = item
            smallest_index = index

    return smallest, smallest_index 


def selection_sort(arr):
    new_array = []
    copy_array = arr.copy()
    for i in range(len(copy_array)):
        smallest, smallest_index = find_smallest_element(copy_array)
        # print(smallest,)
        new_array.append(copy_array.pop(smallest_index))

    return new_array


if __name__ == '__main__':
    array = [12,23,9,46,3,6,2,23,43,54,65,99]
    new_array= selection_sort(array)
    print(array)
    print(new_array)