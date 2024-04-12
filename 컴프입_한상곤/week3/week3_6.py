def main() :
    n = int(input())
    snakeMatrix = [[0 for i in range(n)] for j in range(n)]
    num = 1
    for j in range(n) : 
        if(j % 2 == 0) :
            for k in range(n) :
                snakeMatrix[j][k] = num
                num += 1
        else :
            for k in range(n - 1, -1, -1) :
                snakeMatrix[j][k] = num
                num += 1
   
    for i in snakeMatrix :
        for j in i :
            print(j, end = " ")
        print()


main()
