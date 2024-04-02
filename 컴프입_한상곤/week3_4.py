import sys
input = sys.stdin.readline

def main() :
    print("숫자를 입력하세요")
    num = int(input())

    if(num == 1) : 
        print("1은 소수가 아닙니다")
    for i in range(2, num) :
        if(num % i == 0) :
            print(f"{num}은 소수가 아닙니다")
            exit()
    print(f"{num}은 소수입니다")
            

main()