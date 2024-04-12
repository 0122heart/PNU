def main() :
    numList = list(map(int, 
                       input("쉼표로 구분된 정수를 여러 개 입력하시오: ").split(',')))
    print(f"입력된 정수의 리스트 : {numList}")
    
    # 정렬하기
    makeSorting(numList)
    print("정렬된 정수의 리스트 : ", end = " ")

    # 정렬된 리스트 출력하기
    for i in numList :
        print(i, end = " ")


def makeSorting(numList) :
    for i in range(len(numList)) :
        for j in range(i + 1, len(numList)) :
            if(numList[j] < numList[i]) :
                numList[i], numList[j] = numList[j], numList[i]
            

main()