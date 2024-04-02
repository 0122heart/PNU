def main() :
    n = int(input())
    numList = [[i for i in range(j, j + n)] for j in range(1, n * n, n)]
    for i in range(len(numList)) :
        # 홀수 행
        if(i % 2) :
            for j in numList[i][::-1] :
                print(j, end = " ")
        # 짝수 행
        else :
            for j in numList[i] :
                print(j, end = " ")
        print()    

main()