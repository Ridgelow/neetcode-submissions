from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    length = len(my_list)
    start = length - 3
    end = length 
    return my_list[start:end:1]


# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
