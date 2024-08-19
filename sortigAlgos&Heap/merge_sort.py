class sortingAlgorithms():
    def merge(self, arr1, arr2):
        firstPoint = 0
        secondPoint = 0
        mergedList = []

        while firstPoint < len(arr1) and secondPoint < len(arr2):
            if arr1[firstPoint] < arr2[secondPoint]:
                mergedList.append(arr1[firstPoint])
                firstPoint +=1
            else:
                mergedList.append(arr2[secondPoint])
                secondPoint +=1

        while firstPoint < len(arr1):
            mergedList.append(arr1[firstPoint])
            firstPoint += 1

        while secondPoint < len(arr2):
            mergedList.append(arr2[secondPoint])
            secondPoint += 1
            

    def mergeSort(self, array):
        if len(array) == 1:
            return array
        
        midPoint = int(len(array)/ 2)
        left = array[:midPoint]
        right = array[midPoint:]
        return self.merge(self.mergeSort(left), self.mergeSort(right))
    
sorting = sortingAlgorithms()
print(sorting.mergeSort([9,1,4,3,2,5,7,6,8]))