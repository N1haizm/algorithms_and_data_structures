class searchAlgos():
    def sequentialSearchUnordered(self, unorderedList, number):
        index = 0
        found = False

        while index < len(unorderedList)-1 and not found:
            if unorderedList[index] == number:
                found = True
            else:
                index+=1

        return found

    def sequentialSearchOrdered(self, orderedList, number):
        index = 0
        found = False
        tooBig = False

        while index < len(orderedList)-1 and not found and not tooBig:
            if orderedList[index] == number:
                found = True
            else:
                if orderedList[index] > number:
                    tooBig = True
                else:
                    index +=1
        return found
    
    def binarySearch(self, orderedList, number):
        firstP = 0
        lastP = len(orderedList) - 1
        found = False

        while firstP <= lastP and not found:
            midP = (lastP + firstP) // 2
            if orderedList[midP] == number:
                found = True
            else:
                if orderedList[midP] > number:
                    lastP = midP - 1
                else:
                    firstP = midP + 1
        return found


myList = [60, 30, 40,5 ,80, 13, 73]
myList.sort()
search = searchAlgos()
print(search.binarySearch(myList,73))