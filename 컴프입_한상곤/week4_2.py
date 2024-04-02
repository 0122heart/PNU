def main() :
    src = input()
    now = ""
    for i in src :
        # 정수라면
        if(i.isdigit()) :
            print(now * int(i), end = "")
        # 문자라면
        else :
            now = i

main()