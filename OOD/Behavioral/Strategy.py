# Lets you define a family of algorithms,
# put each of them into a separate class,
# and make their objects interchangeable.

from abc import ABC, abstractmethod
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list) -> list:
        pass

class QuickSort(SortStrategy):
    def sort(self, data:list)->list:
        if len(data) <=1: return data
        pivot = data[len(data)//2]
        left = [x for x in data if x < pivot]
        mid = [x for x in data if x==pivot]
        right = [x for x in data if x>pivot]
        return self.sort(left) + mid + self.sort(right)

class MergeSort(SortStrategy):
    def sort(self, data:list)->list:
        pass

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort(self, data:list)->list:
        return self._strategy.sort(data)

sorter =Sorter(QuickSort())
print(sorter.sort([3,1,4,1,5]))
