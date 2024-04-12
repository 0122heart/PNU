factorialList = [1] + [0 for i in range(19)]

def main() :
    print(f"euler( 5) = {euler(5):.5f}")
    print(f"euler(20) = {euler(20):.5f}")

def euler(num) :
    result = 1
    for i in range(1, num + 1) :
        result += 1/factorial(i)
    return result

def factorial(num) :
    result = 1
    for i in range(1, num + 1) :
        result *= i
    return result

main()