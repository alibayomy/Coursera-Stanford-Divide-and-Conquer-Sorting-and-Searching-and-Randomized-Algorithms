
file = open('nums.txt')
nums = [int(num) for num in file]


def partition(arr,l,r):
   
    first_element = arr[l]
    tmp = arr[l]
    arr[l] = first_element
    arr[r-1] = tmp
    pivot = arr[l]
    i = l + 1
    j = i 
    while j < r:
            if arr[j] <= pivot:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                i += 1
            j += 1
    temp = arr[l]
    arr[l] = arr[i-1]
    arr[i-1] = temp
    return i


def quick_sort(arr, low, high):
    if (arr[low:high] == []):
        return 0
    if low < high:
        total = (high-low -1)
        i = partition(arr, low,high)
        calc_left = quick_sort(arr,low,i -1 )
        calc_right = quick_sort(arr,i,high )
        return total + calc_left + calc_right

print(quick_sort(nums,0, len(nums)))


