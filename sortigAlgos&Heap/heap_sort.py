class sortingAlgorithms():
    def heapify(self,array,n,i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and array[largest] < array[l]:
            largest = l

        if r < n and array[largest] < array[r]:
            largest = r 

        if largest != i:
            array[largest], array[i] = array[i], array[largest]
            self.heapify(array, n, largest)
        
    def heapSort(self, array):
        n = len(array)

        for i in range(n, -1,-1):
            self.heapify(array,n,i)

        for i in range(n-1, 0, -1):
            array[i], array[0] = array[0], array[i]
            self.heapify(array, i, 0)
        
        return array

sorting = sortingAlgorithms()
print(sorting.heapSort([9,1,4,3,2,5,7,6,8]))