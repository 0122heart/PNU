num_func = int(input())
dict_term = {}
for i in range(num_func) :
    num_term = int(input())

    for j in range(num_term) :
        coefficient, exponent = map(int, input().split()) # 계수, 지수 입력받기

        if(exponent in dict_term.keys()) :
            dict_term[exponent] += coefficient # 지수를 key값으로 입력받기
        else :
            dict_term[exponent] = coefficient # 지수를 key값으로 입력받기

keys_to_remove = [key for key, value in dict_term.items() if value == 0] # 계수가 0인 것들 삭제

for key in keys_to_remove:
    del dict_term[key]


if(dict_term) :
    print(len(dict_term.keys()))
    keys = [i for i in dict_term.keys()]
    keys.sort(reverse = True)
    for j in keys :
        print(dict_term[j], j)
else :
    print("0 0")
