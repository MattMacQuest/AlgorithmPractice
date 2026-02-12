class Application:
    def __init__(self):
        self.current_lists = {
            "Unsorted": [],
            "Sorted": []
        }
        self.past_lists = {
            "Unsorted": [],
            "Sorted": []
        }
        
        self.sorting_time = None
        self.list_generation_time = None
        
    # This method will be very memory-heavy, and with no current way to reload lists to reuse
    # it would be better to instead just store past list sizes and maybe performance data after sorting.
    # For now, this will work for both sorted and unsorted doubly so since for me memory isn't an issue
    # Currently unused
    def set_unsorted(self, unsorted_list):
        if self.current_lists["Unsorted"]:
            self.past_lists["Unsorted"].append(self.current_lists["Unsorted"])
            self.current_lists["Unsorted"] = unsorted_list
        else:
            self.current_lists["Unsorted"] = unsorted_list
            
    def set_sorted(self, sorted_list):
        if self.current_lists["Sorted"]:
            self.past_lists["Sorted"].append(self.current_lists["Sorted"])
            self.current_lists["Sorted"] = sorted_list
        else:
            self.current_lists["Sorted"] = sorted_list
            
    def show_past_lists(self):
        pass
    
    # Show past benchmarks and their associated info, like list size, sorting algo used, and time to complete
    def show_benchmark_history(self):
        pass
    
    # Display approx how much memory the lists are taking up
    def show_list_memory_usage(self):
        pass