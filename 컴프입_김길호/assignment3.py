def main() :
    numList = [int(input()) for _ in range(10)]
    selectionSort(numList)
    for i in numList : print(i, end = " ")

def selectionSort(numList) :
    for i in range(len(numList)) :
        minValueIndex = i
        for j in range(i + 1, len(numList)) :
            if(numList[j] < numList[minValueIndex]) :
                minValueIndex = j
        numList[i], numList[minValueIndex] = numList[minValueIndex], numList[i]

main()