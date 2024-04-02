def main() :
    for i in range(1, 10001) :
        if(x := isPerfectNum(i)) : 
            print(f"{i}는 완전수입니다.")
            print(f"{i}의 약수 : {x}, 약수의 합 = {i}")
            print()

def isPerfectNum(num) :
    divisor = set()
    for i in range(1, round(num**(1/2)) + 1) :
        # 나누어 떨어진다면 약수로 추가
        if(num % i == 0) :
            divisor.add(i)
            divisor.add(num // i)
    
    if(sum(list(divisor)) == num * 2) :
        return list(divisor)
    else :
        return 


main()