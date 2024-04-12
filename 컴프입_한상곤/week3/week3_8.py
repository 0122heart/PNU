def main() :
    n = input()
    for i in range(len(n)//2) :
        if(n[i] != n[- 1 - i]) :
            print(f"{n}은(는) 거꾸로 정수가 아닙니다.")
            break
    else :
        print(f"{n}은(는) 거꾸로 정수입니다.")

main()
