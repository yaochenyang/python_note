def findstr(total, target):
    count = 0
    length = len(total)
    if target not in total:
        print('该项中不含这两个字符')
    else:
        for i in range(length - 1):  #因为是查询两个字符的字符串,如果倒数第二个不是其中之一,最后一个也不必查询了
            if (total[i] == target[0]) and (total[i + 1] == target[1]):
                count += 1
    print(count)


total = input('请输入总字符串')
target = input('请输入要查询的两位字符串')
findstr(total, target)
