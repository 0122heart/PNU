def main() :
    birthDay = input("주민등록번호 첫 6숫자 형식 입력: ")
    year = int(birthDay[:2])
    month = int(birthDay[2:4])
    day = int(birthDay[4:])
    if(year < 50) :
        print("20{}년 {}월 {}일".format(year, month, day))
    else :
        print("19{}년 {}월 {}일".format(year, month, day))

main()