# def quick_sort(nums, low, high):
#     if low < high:
#         middle = quick_sort_partition(nums, low, high)
#         quick_sort(nums, low, middle - 1)
#         quick_sort(nums, middle + 1, high)
#     return nums

def quick_sort(nums, low, high):
    while(low < high):
        pivot = nums[(low + high) // 2]
        i = low
        j = high
        while(i <= j):
            while(nums[i] < pivot):
                i += 1
            while(nums[j] > pivot):
                j -= 1
            if(i > j):
                break
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        if((j - low) <= (high - i)):
            quick_sort(nums, low, j)
            low = i
        else:
            quick_sort(nums, i, high)
            high = j
    return nums

# def quick_sort_partition(nums, low, high):
#     pivot = nums[high]
#     i = low - 1
#     for j in range(low, high):
#         if nums[j] < pivot:
#             i += 1
#             nums[i], nums[j] = nums[j], nums[i]
#     nums[i + 1], nums[high] = nums[high], nums[i + 1]
#     return i + 1

def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    return nums

def bubble_sort(app):
    sorted_list = app.current_lists["Unsorted"].copy()
    swapping = True
    end = len(sorted_list)
    while swapping:
        swapping = False
        for i in range(1, end):
            if sorted_list[i - 1] > sorted_list[i]:
                sorted_list[i - 1], sorted_list[i] = sorted_list[i], sorted_list[i - 1]
                swapping = True
        end -= 1
    app.current_lists["Sorted"] = sorted_list