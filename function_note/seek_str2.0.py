str1 = '''ABSaDKSbRIHcRHGcdDIF'''

countA = 0  # 统计前边的大写字母
countB = 0  # 这个是用来统计小写主字符的
countC = 0  # 这个是用来统计右边大写字符个数的
length = len(str1)

for i in range(length):
    if str1[i] == '\n':
        continue
    if str1[i].isupper():
        if countB:  # 这句意思就是说小写字符已经就位的情况下再探测出大写字符则该大写字符为小写字符右边的大写字符 所以countC+=1
            countC += 1
        else:  # 这句就是小写字符b没有就位的情况下 则探测到的大写字符 为小写字符左边的大写字符 所以countA += 1
            countA += 1
            countC = 0  # 小写字符b都没有就位所以 countC则自然而然的清零一次
    if str1[i].islower():  # 这句的意思就是左边大写字符A都没集齐三个的情况下出现了小写字符,所以不符合题意 作清除处理.
        if countA != 3:
            countA = 0
            countB = 0
            countC = 0
        else:  # 这个else:也就是说countA == 3 也就是说已经是集齐了左边的三个大写字时符的情况
            if countB:  # 这句说的又是已经有了小写字符,探测出的还是小写字符,所以清零
                countA = 0
                countB = 0
                countC = 0
            else:  #   == 0
                countB = 1  # 没有小写字符的时候直接给B添加一个
                countC = 0
                target = i  # 存入小写字母的索引
    if countA == 3 and countC == 3:
        if i + 1 != length and str1[i + 1].isupper():
            countB = 0
            countC = 0
        else: 
            print(str1[target], end='')
            countA = 3
            countB = 0
            countC = 0
