# problem_1 ###############################################

def sum_of_odd(numList) :
    # 값이 없는 경우
    if(numList) :
        result = 0
        for i in numList : 
            # 음수가 존재하면 0 return
            if(i < 0) :
                return 0
            
            # 홀수이면
            if(i % 2) :
                result += i

        return result

    return 0

# problem_2 ###############################################

def is_find_element_in_matrix(matrix, target) :
    for i in matrix :
        for j in i :
            if(target == j) :
                return True
    return False


# problem_3 ###############################################

def pascal_triangle(num) :
    numList = []
    for i in range(num + 1) :
        numList.append(calculate(num, i))
    return numList

def calculate(n, r) :
    if(n == r or r == 0) :
        return 1
    else :
        return calculate(n - 1, r - 1) + calculate(n - 1, r)


# problem_4 ###############################################

def count_mean_over(mean, score) :
    count = 0

    for i in score :
        total = 0
        for j in i :
            total += j
        if(3 * mean <= total) :
            count += 1

    return count


# problem_5a ###############################################

def discriminant(input) :
    a, b, c = input
    return b * b - 4 * a * c

# problem_5b ###############################################

def quadratic(input) :
    judge = discriminant(input)
    a, b, c = input

    # 음수 반환
    if(judge < 0) :
        return None

    # 양수 반환
    elif(judge) :
        result1 = -b + judge ** (1/2)
        result2 = -b - judge ** (1/2)
        return result1 / 2 / a, result2 / 2 / a
    
    else :
        result = -b / 2 / a
        return result, result


############################################################# 
