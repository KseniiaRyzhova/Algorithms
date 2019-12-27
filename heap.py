
import numpy


class Heap:

    def __init__(self):
        pass

    def get_Heap_height(self, arr):
        height = 0
        if len(arr) == 0: return 0
        i = 0
        while 2*i+1 <=len(arr):
            height+=1
            i+=1
        return height

    # The main function to sort an array of given size
    def sort_heap(self, arr, new_arr):
        if len(arr) == 0: return new_arr
        sort_arr = self.max_heap(arr)
        sort_arr = self.__swapList(sort_arr)
        new_arr.insert(0, sort_arr[-1])
        return self.sort_heap(sort_arr[:-1], new_arr)


    def __swapList(self, newList):
        """Fuunction to swap first and last element of a list"""
        size = len(newList)

        # Swapping
        temp = newList[0]
        newList[0] = newList[size - 1]
        newList[size - 1] = temp

        return newList

    def max_heap(self, arr):
        max_heap_arr = arr
        height = self.get_Heap_height(max_heap_arr)
        for i in range(0, height-1):
            left =  None if 2*i+1 >=len(arr) else arr[2*i+1]
            right =  None if 2*i+2 >=len(arr) else arr[2*i+2]
            if left == None:
                pass
            elif max_heap_arr[i] < left:
                temp = max_heap_arr[i]
                max_heap_arr[i] = left
                max_heap_arr[2*i+1] = temp
            if  right==None:
                pass
            elif max_heap_arr[i] < right:
                temp = max_heap_arr[i]
                max_heap_arr[i] = right
                max_heap_arr[2*i+2] = temp
        return max_heap_arr
