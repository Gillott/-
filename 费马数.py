#一段用于推翻费马数猜想的代码
#放在GitHub上主要是用来研究GitHub的使用方法
n = 0
while True:
    n += 1
    s = 2**2**n+1
    for i in range(2,s):
        if s % i == 0:
            print("第"+str(n)+"个数"+str(s)+"不满足费马猜想，"+
            "该数可被"+str(i)+"整除。")
            break
        else:
            continue