def main() :
    src = input()
    now = ""
    num = 0

    for i in src :
        # 문자열이 연속되고 있다면
        if(i == now) :
            num += 1
        # 문자열이 끊어졌다면
        else :
            if(num) :
                print(now + str(num), end = "")
            now = i
            num = 1

    print(now + str(num))
            
main()