def main() :
    x1 = int(input("x1 좌표를 입력하시오 : "))
    y1 = int(input("y1 좌표를 입력하시오 : "))
    x2 = int(input("x2 좌표를 입력하시오 : "))
    y2 = int(input("y2 좌표를 입력하시오 : "))
    print(f"두 점의 거리 : {distance(x1, y1, x2, y2)}")

def distance(x1, y1, x2, y2) :
    horizon = x1 - x2
    vertical = y1 - y2
    diagonal = (horizon ** 2 + vertical ** 2)**(1/2)
    return diagonal


main()