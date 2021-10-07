from dataclasses import dataclass


@dataclass
class Sorting(object):
    random_arr: []

    @property
    def random_arr(self) -> []:  # not str or list
        return self._random_arr

    @random_arr.setter
    def random_arr(self, random_arr):
        self._random_arr = random_arr  # "_~" only for internal ref

    def bubble_sort(self):
        arr = self.random_arr
        n = len(arr)
        for i in range(n - 1):  # n-1 because loop is -1 less than total num of input
            for j in range(n - i - 1):  # that next number
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(arr)
        return arr

    @staticmethod  # rids limits in def ~(x_self)
    def merge_sort(arr: []):
        if len(arr) < 2:
            return arr
        mid = len(arr) // 2  # division operator. "//" divs + rounds down.
        low = Sorting.merge_sort(arr[:mid])
        high = Sorting.merge_sort(arr[mid:])
        arr = []
        low_index = hi_index = 0

        while low_index < len(low) and hi_index < len(high):
            if low[low_index] < high[hi_index]:
                arr.append(low[low_index])
                low_index += 1
            else:
                arr.append(high[hi_index])
                hi_index += 1
        arr += low[low_index:]
        arr += high[hi_index:]  # appending
        print(arr)
        return arr

    @staticmethod
    def quick_sort(arr: []):
        if len(arr) <= 2:
            return arr
        pivot = len(arr) // 2
        left, pivot_arr, right = [], [], []
        for value in arr:
            if value < arr[pivot]:
                left.append(value)
            elif value > arr[pivot]:
                right.append(value)
            else:
                pivot_arr.append(value)
        print(left, pivot_arr, right)
        return Sorting.quick_sort(left) + Sorting.quick_sort(pivot_arr) + Sorting.quick_sort(right)
