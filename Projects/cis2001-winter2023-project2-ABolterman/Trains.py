class Train:
    def __init__(self, num_items, train_number):
        self._items_needed = int(num_items)
        self._items_loaded = 0
        self._time_departed = None
        self._number = train_number

    def add_item(self, time):
        self._items_loaded += 1
        time += self._number
        if self._items_loaded == self._items_needed:
            self._time_departed = time
        time += self._number
        return time

    def get_time_departed(self):
        return self._time_departed
