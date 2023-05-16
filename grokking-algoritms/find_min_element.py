def find_smallest_element(arr):
    smallest = arr[0]
    smallest_index = 0

    for index, item in enumerate(arr):
        if smallest > item:
            smallest = item
            smallest_index = index

    return smallest, smallest_index 




if __name__ == '__main__':
    array = [12,23,9,46,3,6,2,23,43,54,65,99]
    item, index = find_smallest_element(array)
    print(item, index)