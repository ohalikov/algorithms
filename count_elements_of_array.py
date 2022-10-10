def count_elements_of_array(array):    
    if array == []:
        return 0
    else:
        return 1 + count_elements_of_array(array[:-1])


if __name__ == '__main__':
    array = [4,3,4,3,5]
    counter = count_elements_of_array(array)
    print(counter)