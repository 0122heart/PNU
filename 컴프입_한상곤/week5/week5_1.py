def main() :
    for i in range(10, 51, 10) :
        print(f"섭씨온도 {i}C의 화씨온도는 {cel2fah(i)}F입니다 ")

def cel2fah(cel) :
    return cel * 9 / 5 + 32

main()