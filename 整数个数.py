

class Ze():
    def __init__(self,m,n):
        self.m = m
        self.n = n

    def sgn(self,x):
        if x > 0:
            return 1
        elif x == 0:
            return 0
        else:
            return -1
    def get_the_result(self):
        a = self.sgn(self.n-int(self.n))
        return int(self.n - self.m + 1 - a)

variable = input("此程序用于给出闭区间[m,n]所覆盖数轴上整数的个数，\n请以此输入m,n的数值（需保证n-m为正整数）：").split(",")

v = [variable[i] for i in range(len(variable))]
m = v[0]
n = v[1]
d = float(n)-float(m)
if d % 1 == 0:
    result = Ze(float(m),float(n)).get_the_result()
    print("闭区间[m,n]所覆盖数轴上整数的个数为：" + str(result))
else:
    print("鬼！你输入的不符合要求！")







    
    
    

