
file = open('IntegerArray.txt',"r")
lst = []
for line in file:
    lst.append(int(line))


def count_inversions(lst):

    if len(lst) <= 1:
        return 0
    mid = len(lst) // 2
    left_arr = lst[:mid]
    right_arr = lst[mid:]
    left_inv = count_inversions(left_arr)
    right_inv = count_inversions(right_arr)

    split_inv = 0
    left_index = 0
    right_index = 0
    final_output_index = 0

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            lst[final_output_index] = left_arr[left_index]
            left_index += 1
            final_output_index += 1
        else:
            lst[final_output_index] = right_arr[right_index]
            split_inv += len(left_arr[left_index:])
            right_index += 1
            final_output_index += 1
    while left_index < len(left_arr):
        lst[final_output_index] = left_arr[left_index]
        final_output_index += 1
        left_index += 1
    while right_index < len(right_arr):
        lst[final_output_index] =right_arr[right_index]
        final_output_index += 1
        right_index += 1
    return split_inv + left_inv + right_inv

print(count_inversions(lst))

