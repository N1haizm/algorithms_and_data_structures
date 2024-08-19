class sortingAlgorithms():
    def insertionSort(self, array):
        for i in range(1,len(array)):
            tamp = array[i]
            j = i - 1
            while tamp < array[j] and j > -1:
                array[j+1] = array[j]
                array[j] = tamp
                j-=1
        return array

sorting = sortingAlgorithms()
print(sorting.insertionSort([9,1,4,3,2,5,7,6,8]))