class sortingAlgorithms():
    
    def bubbleSort(self, array):
        for i in range(len(array)-1, 0, -1):
            for j in range(i):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                
        return array
    
sorting = sortingAlgorithms()
print(sorting.bubbleSort([9,1,4,3,2,5,7,6,8]))
