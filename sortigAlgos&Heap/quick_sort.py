class sortingAlgorithms():
    def pivot(self, arr, pivotIndex,endIndex):
        swapIndex = pivotIndex
        for i in range(pivotIndex+1,endIndex+1):
            if arr[i] < arr[pivotIndex]:
                swapIndex +=1
                arr[swapIndex], arr[i] = arr[i], arr[swapIndex]
        arr[pivotIndex], arr[swapIndex] = arr[swapIndex], arr[pivotIndex]
        return swapIndex

    def quickSort(self, array, leftPoint = 0, rightPoint = None):
        if rightPoint == None:
            rightPoint = len(array) - 1
        if leftPoint < rightPoint:
            swapIndex = self.pivot(array, leftPoint, rightPoint)
            self.quickSort(array, leftPoint, swapIndex-1)
            self.quickSort(array, swapIndex+1, rightPoint)
        return array
    

sorting = sortingAlgorithms()
print(sorting.quickSort([9,1,4,3,2,5,7,6,8]))
        