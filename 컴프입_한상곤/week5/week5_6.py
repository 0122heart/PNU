def main() :
    while(1) :
        r = int(input("반지름을 입력하시오: "))
        if(0 < r) :
            area, perimeter = area_and_circumference(r)
            print("넓이 : {:.3f}, 둘레 : {:.3f}".format(area, perimeter))
        else :
            print("프로그램을 종료합니다.")
            break


def area_and_circumference(r) :
    area = r * r * 3.141592
    perimeter = 2 * r * 3.141562
    return area, perimeter

main()