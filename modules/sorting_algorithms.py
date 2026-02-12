def quick_sort(app):
    pass

def insertion_sort(app):
    pass

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