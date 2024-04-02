import sys
input = sys.stdin.readline

def main() :
    x = int(input("x좌료를 입력하세요"))
    y = int(input("y좌표를 입력하세요"))

    if(x == 0 or y == 0) : 
        print("AXIS")
    elif(0 < x) :
        if(0 < y) :
            print("1Q")
        else :
            print("4Q")
    else :
        if(0 < y) :
            print("2Q")
        else :
            print("3Q")
            

main()