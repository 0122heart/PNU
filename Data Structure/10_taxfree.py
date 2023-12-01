def main() :
    N, coupon = map(int, input().split())

    values = [] # 면세품 가격들

    for i in range(N) :
        values.append(int(input()))

    values.sort()

    num_items = 0

    for i in range(1, len(values)) : # 최대 몇개까지 가능한지 체크
        if(sum(values[:i]) <= coupon) :
            num_items = i
        else :
            break

    if(num_items == 1) : # 최대 한개까지 가능할 경우
        if(coupon not in values) :
            print(0)
        else : 
            print(coupon)

    else : # 두 개 이상까지 가능할 경우
        combination = []

        if(coupon in values) : # 한개의 조합
            combination.append([coupon])

        for i in range(2, num_items + 1) :
            for j in f_combination_recursive(i, values, coupon) : 
                combination.append(j)

        if(combination) : 
            for i in combination : 
                i.sort(reverse = True)
            
            combination.sort(reverse = True)
            
            combination[0].sort()

            for i in combination[0] : 
                print(i)
                
        else : 
            print(0)


def f_combination_of_two(values, coupon) :
    ''' 두 개 조합 구하기 '''

    start = 0; end = len(values) - 1
    combination = []

    while(start < end) :
        result = values[start] + values[end]
        if(result < coupon) :
            start += 1
        elif(result == coupon) :
            combination.append([values[start], values[end]])
            start += 1
            end -= 1
        else :
            end -= 1

    return combination

def f_combination_recursive(num_items, values, coupon) :
    combination = []

    if(num_items == 2) :
        return f_combination_of_two(values, coupon)
    
    else :
        start = 0
        while(start <= len(values) - num_items) :
            temp_value = values[start]
            for i in f_combination_recursive\
                (num_items - 1, values[start + 1:], coupon - temp_value) :
                combination.append([temp_value] + i)
            start += 1
            
        return combination

main()



