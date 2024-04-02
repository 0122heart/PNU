import sys
input = sys.stdin.readline

def main() : 
    num1 = int(input("숫자를 입력하세요"))
    num2 = int(input("숫자를 입력하세요"))
    num3 = int(input("숫자를 입력하세요"))
    
    numbers = []

    # num1 < num2
    if(num1 < num2) :
        # num1 < num2 <= num3
        if(num2 <= num3) : 
            print(num1, num2, num3)
        # num1 ? num3 < num2
        else : 
            # num1 <= num3 < num2
            if(num1 <= num3) :
                print(num1, num3, num2)
            # num3 < num1 < num2
            else :
                print(num3, num1, num2)
    # num1 == num2
    elif(num1 == num2) :
        # num1 == num2 <= num3
        if(num1 <= num3) : 
            print(num1, num2, num3)
        # num3 < num1 < num2
        else :
            print(num3, num1, num2)
    # num2 < num1
    else :
        # num2 < num1 <= num3
        if(num1 <= num3) :
            print(num2, num1, num3)
        # num2 ? num3 < num1
        else :
            # num2 <= num3 < num1
            if(num2 <= num3) :
                print(num2, num3, num1)
            # num3 < num2 < num1
            else :
                print(num3, num2, num1)



main()