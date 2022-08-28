l1 = int(input())
h1 = int(input())
s1 = int(input())

l2 = int(input())
h2 = int(input())
s2 = int(input())

n1 = (l1 // l2) * (h1 // h2) * (s1 // s2)
n2 = (l1 // h2) * (h1 // l2) * (s1 // s2)
n3 = (l1 // l2) * (h1 // s2) * (s1 // h2)
n4 = (l1 // s2) * (h1 // l2) * (s1 // h2)
n5 = (l1 // s2) * (h1 // h2) * (s1 // l2)
n6 = (l1 // h2) * (h1 // s2) * (s1 // l2)

if n1 > n2:
    n1, n2 = n2, n1
if n2 > n3:
    n2, n3 = n3, n2
if n1 > n2:
    n1, n2 = n2, n1
if n4 > n5:
    n4, n5 = n5, n4
if n5 > n6:
    n5, n6 = n6, n5
if n4 > n5:
    n4, n5 = n5, n4
if n3 > n6:
    print(n3)
else:
    print(n6)
