class sortingAlgorithms():
    def selectionSort(self, array):
        for i in range(len(array)-1):
            minIndex = i
            for j in range(i+1,len(array)):
                if array[j] < array[minIndex]:
                    minIndex = j
            if i != minIndex:
                array[i], array[minIndex] = array[minIndex], array[i]
        return array

sorting = sortingAlgorithms()
print(sorting.selectionSort([9,1,4,3,2,5,7,6,8]))