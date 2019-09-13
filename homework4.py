# 1:读取成绩并输出成绩等级
# def scores(a,b,c,d):
#    x = [a,b,c,d]
#    y = sorted(x)
#    best = y[3]
#    for i in range(len(x)):
#        if x[i] >= best - 10:
#            print('成绩为A')
#        elif x[i] >= best - 20:
#            print('成绩为B')
#        elif x[i] >= best - 30:
#            print('成绩为C')
#        elif x[i] >= best - 40:
#            print('成绩为D')
#        else:
#            print('成绩为F')
# scores(40,55,70,58)



# 2：逆序顺序显示一个整数列表：
#a = [1,2,3,4,0,9,8,7]
#b = a[::-1]
#print(b)






# 3:读取1到100之间的一些整数，并统计每个数的个数
# def occurso():
#    str1 = [1,2,3,4,5,4,3,5,3,2,4,2]
#    str2 = [1,2,3,4,5,4,3,5,3,2,4,2]

#    for i in range(len(str1)):
#        num1 = 0
#        for j in range(len(str2)):
#            if str2[j] == str1[i]:
#                num1 += 1
#            else:
#                num1 = num1
#        print(num1)
# occurso()




# import random
# ls = list()
# ls = [random.randint(0,100) for i in range(15)]
# st = set(ls)
# for i in st:
#     print(i, '出现的次数为： ', ls.count(i))



# 4:计算有多少是大于平均数有多少是小于平均数的
#def average(list):
#    pinjun = sum(list)/(len(list)*1.0)
#    return pinjun
#num1 = 0
#num2 = 0
#def fenshu(list_):
#    pinjun = average(list_)
#    for i in range(len(list_)):
#        
#        global num1
#        global num2
#        if list_[i] > pinjun: 
#            num1 += 1
#        elif list_[i] < pinjun:
#            num2 += 1
#        else:
#            pass
#    print(num1)
#    print(num2)
#    print(pinjun)
#fenshu([2,4,2,4,8])



##6：返回最小元素的下标
#def indexOFSmallestElement(lst):
#    lst1 = lst
#    lst2 = sorted(lst)
#    zuixiao = lst2[0]
#
#    for i in range(len(lst1)):
#        if lst1[i] == zuixiao:
#            print('最小元素的下标再第几个呢，就是这里>>%d'%(i+1))
#            
#indexOFSmallestElement([3,4,2,7,5,4,1,4,3,4])