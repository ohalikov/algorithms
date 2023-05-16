def binary_search(list, item):
    low = 0
    high = len(list)-1

    while(low <= high):
        mid = round((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1

    return None


my_list = [1,3,5,7,9,11,13]
index_position = binary_search(my_list, 7)

print(index_position)