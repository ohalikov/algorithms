def find_smallest_element(current_array):
    smallest_element = current_array[0]
    smallest_index = 0

    for index, current_element,  in enumerate(current_array):
        if current_element < smallest_element:
            smallest_element = current_element
            smallest_index = index
    
    return smallest_index, smallest_element


def choosing_sort(current_array):
    new_sorted_array = []
    copy_current_array = current_array.copy()
    for i in range(len(current_array)):
        smallest_index, smallest_element = find_smallest_element(copy_current_array)
        dropped_element = copy_current_array.pop(smallest_index)
        new_sorted_array.append(dropped_element)


    return new_sorted_array


if __name__ == '__main__':
    array = [12,23,9,46,3,6,2,23,43,54,65,99]
   
    index, smallest_element = find_smallest_element(array)
    print(f'{smallest_element=} -> {index=}')

    new_sorted_array = choosing_sort(array)
    print(new_sorted_array)