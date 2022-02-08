a = int(input())
b = int(input())
c = int(input())

a_odd = a % 2
b_odd = b % 2
c_odd = c % 2

a_even = not (a % 2)
b_even = not (b % 2)
c_even = not (c % 2)

if (a_odd or b_odd or c_odd) and (a_even or b_even or c_even):
    print("YES")
else:
    print("NO")
