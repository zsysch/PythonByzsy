#print('hello world')
# num1=float (input("请输入数字"))
# num2=float (input('请输入另一个数字'))
# print(num1 * num2)

# email = 'PST@222.com'
# for e in email:
#     O = ord (e)
#     # print(O)

# a = (input('请说出你想说的话：'))
# b = ('你说的太对了')
# # print (b)

# 输入一个年份判断是否为闰年
# year = int (input('请输入一个年份：>>'))
# if year % 4 == 0 and year % 100 !=0 or year % 400 == 0:
#     print('%d 是闰年' %year)
# else:
#     print('
#  不是闰年' %year)

# 将华氏度转为摄氏度
# f = float(input('请输入华氏温度'))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f,c))  #这里的%是插入的意思，将输出的(华氏度)插入 %(f,c)中的f.  %.1f 表示精确到小数点后一位.


# 水仙花
# Number = input('请输入一个数字：')
# bai = int(Number[0])
# shi = int(Number[1])
# ge = int(Number[2])
# if bai **3 + shi **3 +ge **3 == int(Number):
#     print('是水仙花')
# else:
#     print('不是水仙花')

# 从控制台读取摄氏温度并将它转变为华氏温度并予以显示。
# c = float(input('请输入摄氏温度：'))
# f = (9/5)*c+32
# print('%.2f摄氏度 = %.2f华氏度' %(c,f))

# # 读取与圆柱的半径和高，计算圆柱体底面积和体积
# import math
# radius = float(input('请输入圆柱的半径'))
# area = radius * radius * math.pi
# print('该圆柱的底面积为： %.2f' %area )
# length = float(input('请输入该圆柱体的高：'))
# volume = area * length
# print('该圆柱体的体积为：%.2f' %volume)

# 将读取的英尺数转换为米数并显示
# feet = float(input('请输入英尺数：'))
# meter = feet * 0.305
# print('对应的米数为：%.4f ' % meter)
# print('%.3f英尺数 = %.4f米数' %(feet,meter))

# 计算将水从初始温度加热到最终温度所需要的能量。
# m = float(input('请输入水的质量：'))
# finaltemperature = float(input('请输入最终温度：'))
# initialtemperature = float(input('请输入初始温度'))
# Q = m * (finaltemperature - initialtemperature) * 4184
# print('所需能量为：%.1f' %Q)

# 计算下个月月供的利息
# balance = float(input('请输入差额：'))
# rate = float(input('请输入年利率：'))
# interest = balance * (rate/1200)
# print('下个月的利息为: %.5f' %interest)

# 求加速度
# v0 = float(input('请输入初始速度：'))
# v1 = float(input('请输入末速度：'))
# t = float(input('请输入所占时间：'))
# a = (v1-v0) / t
# print('平均加速度为:%.4f' %a)

# 复利值
# amount = input('请输入存钱金额:')
# sum = 0
# for i in range(6):
#     sum = (sum+float(amount)) * (1 + 0.00417)
# print('6个月之后，账户值为： %.2f'%sum)

# 计算一个整数中各数字之和
num = int(input("请输入0-1000之间任意整数："))
if num < 0 and num > 1000:
    print('输入有误')
else:
    a = int(num % 100)
    b = a % 10 
    c = int(a / 10) 
    d = int(num / 100) 
    sum = b + c + d
print('数字的和为： %d'%sum)

