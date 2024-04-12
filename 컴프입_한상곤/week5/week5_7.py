def main() :
    fraction = float(input("1보다 작고 0보다 큰 소수를 입력하세요: "))
    nearest = unit_fraction(fraction)
    print("가장 가까운 단위 분수는 1/{}이며, 이 값은 {}입니다.".format(nearest, 1/nearest))

def unit_fraction(frac) :
    # 소수 부분이 내림됨
    flooredDenominator = int(1/frac)
    
    # 소수 부분이 올림됨
    ceiledDenominator = flooredDenominator + 1

    # 차이가 더 작은 것을 return
    if(abs(frac - 1/flooredDenominator) < abs(frac - 1/ceiledDenominator)) : 
        return flooredDenominator
    else :
        return ceiledDenominator

    

main()