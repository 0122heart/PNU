# problem 0
def final_00(x, y) :
    return str(x + y)

# problem 1
def final_01(num, result = "") :
    num = str(num)
    result += num[0]
    num = num[1:]
    
    # 종료 조건
    if(len(num) == 0) :
        return result
    
    # 종료가 아닐 시 재귀
    if(len(num) % 3 == 0) :
        return final_01(num, result + ",")
    else :
        return final_01(num, result)
    
# problem 2
def final_02(decimalList) :
    result = 0
    for i in decimalList :
        result = result * 10 + i
    return [int(i) for i in str(result + 1)]

# problem 3
def final_03(start, end) :
    return [i for i in range(start, end + 1) if((i % 4 == 0 and i % 100 != 0) or (i % 400 == 0))]

# problem 4
def final_04(word, repeat) :
    return [word[i:i + repeat] for i in range(len(word) - repeat + 1)]

# problem 5
def final_05(matrix, standard) :
    more = [j for i in matrix for j in i if(standard <= j)]
    return (len(more), sum(more))
