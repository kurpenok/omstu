def number_of_divisors(divisor: int) -> int:
    global requests
    global divisors

    if divisor in divisors:
        return divisors[divisor]

    requests.add(divisor)
    
    count = 2

    for i in range(2, int(divisor**0.5) + 1):
        if not (divisor % i):
            count += 2
    
    divisors[divisor] = count
    
    return count


if __name__ == "__main__":
    requests = set()
    divisors = {}

    print(number_of_divisors(2000000000))
    print(number_of_divisors(6))
    print(number_of_divisors(6))
    print(number_of_divisors(2000000000))

    print(divisors)

