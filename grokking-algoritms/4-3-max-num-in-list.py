def get_max_count_in_list(list):
    if len(list) == 2:
        return list[0] if list[0] >= list[1] else list[1]
    
    sub_list = get_max_count_in_list(list[1:])
    print(sub_list)
    return list[0] if list[0] >= sub_list else sub_list


list_array = [1,23,66,4,66,43,77,0,4,65]
print(get_max_count_in_list(list_array))