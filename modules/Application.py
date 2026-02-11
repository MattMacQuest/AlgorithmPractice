class Application:
    def __init__(self):
        self.unsorted_list = []
        self.sorted_list = []
        self.past_lists = {
            "Unsorted": [],
            "Sorted": []
        }
        
        self.sorting_time = None
        self.list_generation_time = None
        
    # This method will be very memory-heavy, and with no current way to reload lists to reuse
    # it would be better to instead just store past list sizes and maybe performance data after sorting.
    # For now, this will work for both sorted and unsorted doubly so since for me memory isn't an issue
    def set_unsorted(self, unsorted_list):
        if self.unsorted_list:
            self.past_lists["Unsorted"].append(self.unsorted_list)
            self.unsorted_list = unsorted_list
        else:
            self.unsorted_list = unsorted_list
            
    def set_sorted(self, sorted_list):
        if self.sorted_list:
            self.past_lists["Sorted"].append(self.sorted_list)
            self.sorted_list = sorted_list
        else:
            self.uorted_list = sorted_list
            
    def show_past_lists(self):
        pass
    
    # Show past benchmarks and their associated info, like list size, sorting algo used, and time to complete
    def show_benchmark_history(self):
        pass
    
    # Display approx how much memory the lists are taking up
    def show_list_memory_usage(self):
        pass