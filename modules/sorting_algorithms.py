def quick_sort(app):
    pass

def insertion_sort(app):
    pass

def bubble_sort(app):
    sorted_list = app.unsorted_list.copy()
    swapping = True
    end = len(sorted_list)
    while swapping:
        swapping = False
        for i in range(1, end):
            if sorted_list[i - 1] > sorted_list[i]:
                sorted_list[i - 1], sorted_list[i] = sorted_list[i], sorted_list[i - 1]
                swapping = True
        end -= 1
    app.sorted_list = sorted_list