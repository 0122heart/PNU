import sys
input = sys.stdin.readline

def main() : 
    print("1에서 9까지의 수를 입력하세요")
    num = int(input())
    while(num < 1 or 9 < num) :
        print("1에서 9까지의 수를 다시 입력하세요")
        num = int(input())

    for i in range(1, 10) :
        print(f"{num} x {i} = {num * i}")

main()