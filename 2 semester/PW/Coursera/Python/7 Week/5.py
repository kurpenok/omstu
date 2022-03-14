maxNum = int(input())
mayList1 = range(1, maxNum + 1)
mayList = set(mayList1)
listNum = 0
while listNum != 'HELP':
    listNum = input()
    if str(listNum) == 'HELP':
        break
    else:
        listNum = list(map(int, listNum.split()))
        guess = set(listNum)
    answer = str(input())
    if answer == 'YES' or answer == 'YES ':
        mayList &= guess
    if answer == 'NO' or answer == 'NO ':
        mayList -= guess
mustList = list(mayList)
mustList.sort()
print(*mustList)
