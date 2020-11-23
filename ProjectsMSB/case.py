# @License : 西安工业大学
# @Author  : 王泽 WZ-Dale
# @Time    : 2020/11/14 13:40

"""实操案例1"""
# 1.向文件中输出数据
# 使用print进行输出
fp=open("test1.txt",'w')
print("Hello Python!!",file=fp)
fp.close()
# 使用文件读写操作
with open("test1.txt",'w',encoding='utf-8') as file:
    file.write("奋斗成就更好的你！！")
# 2.输出北京天气预报
print("星期日","今天")
print("--------------------------------------------")
print("08时","11时","14时","17时","20时","23时")
print("0℃ ","6℃ ","10℃ ","4℃ ","1℃ ","0℃ ")
print("--------------------------------------------")
print("明天","2/23","2℃/11℃")
# 3.机票购买界面
print("❤    ✈    ⊙")
# 4.北京地铁1号线运行图
print("⇌    ⇌    ⇌")

"""实操案例2"""
# 1.输出图书信息
publish="出版社"
print("《",publish,"》")
# 2.输出前五位
name1="赵"
name2="钱"
name3="孙"
name4="李"
name5="周"
print("➊\t"+name1)
print("➋\t"+name2)
print("➌\t"+name3)
print("➍\t"+name4)
print("➎\t"+name5)
print("- - - - - - - - - -")
name_list=["赵","钱","孙","李","周"]
sig_list=["➊","➋","➌","➍","➎"]
for i in range(5):
    print(sig_list[i],"\t",name_list[i])
print("- - - - - - - - - -")
d={"➊":"赵","➋":"钱","➌":"孙","➍":"李","➎":"周"}
for i in d:
    print(i,"\t",d[i])
print("- - - - - - - - - -")
for sig,name in zip(sig_list,name_list):
    print(sig,"\t",name)
# 3.输出图书音像勋章
print("\033[0;35m图书音像勋章\033[m")
# 4.输出身体指标
height=float(input("身高："))
weight=float(input("体重："))
bmi=weight/(height+weight)
print("BMI指数是：",bmi)
print("BMI指数是："+str(bmi))
print("BMI指数是："+"{:0.2f}".format(bmi))
print("BMI指数是：{:0.2f}".format(bmi))

"""实操案例3"""
# 1.进制转换
def fun():
    num=int(input("请输入一个十进制的整数:"))
    print(num,"的二进制数为:",bin(num))    # 个数可变的位置参数
    print(str(num)+"的二进制数为:"+bin(num))    # +的左右均为str
    print("%s的二进制数为:%s"%(num,bin(num)))    # 格式化输出
    print("{0}的二进制数为:{1}".format(num,bin(num)))
    print(f"{num}的二进制数为:{bin(num)}")
    print("-----------------------------------")
    print(f"{num}的八进制数为:{oct(num)}")
    print(f"{num}的十六进制数为:{hex(num)}")
while True:
    try:
        fun()
    except:
        print("只可以输入整数!")
    else:
        break
# 2.手机充值
money=8
print(f"手机余额为:\033[0;35m{money}元\033[m")
money+=int(input("充值:"))
print(f"当前余额为:\033[0;35m{money}元\033[m")
# 3.能量消耗
calorie=28*int(input("当天步数:"))
print(f"消耗卡路里:{calorie},即{calorie/1000}千卡")
# 4.预测子女身高
father_height=float(input("父亲的身高:"))
monther_height=float(input("母亲的身高:"))
son_height=(father_height+monther_height)*0.54
print("子女的身高预测值:{:.2f}cm".format(son_height))

"""实操案例4"""
# 1.支付密码验证
pwd=input("支付宝支付密码：")
if pwd.isdigit():
    print("合法")
else:
    print("不合法")
print("- - - - - - - - - - - - - - -")
print("合法" if pwd.isdigit() else "不合法")
# 2.模拟账号登录
qq=input("请输入账号：")
pwd=input("请输入密码：")
if qq=="123" and pwd=="456":
    print("成功")
else:
    print("失败")
# 3.价格竞猜
import random
price=random.randint(1000,1500)
print("价格区间为：1000-1500")
while True:
    guess=int(input("输入竞猜："))
    if guess>price:
        print("大了")
    elif guess<price:
        print("小了")
    else:
        print("正确！！")
        break
# 4.查看星座运势
d={"狮子座":"双子座","双子座":"狮子座"}
star=input("请输入星座：")
print(f"匹配星座为：{d.get(star)}")    # 使用get方法，即使获取不到也不会报错

"""实操案例5"""
# 1.循环输出26个字母对应的ASCII码值
x=97    # a的ASCII码值
for _ in range(1,27):
    print(chr(x),'--->',x)
    x+=1
print("--------------------------")
x=97
while x < 123:
    print(chr(x),"--->",x)
    x+=1
# 2.模拟用户登录
for i in range(1,4):
    qq = input("请输入账号：")
    pwd = input("请输入密码：")
    if qq == "123" and pwd == "456":
        print("成功")
        break
    else:
        print("失败")
        if i < 3:
            print(f"还有{3-i}次机会")
else:
    print("三次均错误，账号锁定")
# 3.猜数
import random
rand=random.randint(1,100)
for i in range(1,11):
    num=int(input("范围1-100，请猜:"))
    if num < rand:
        print("小了")
    elif num > rand:
        print("大了")
    else:
        print("恭喜你猜对了")
        print(f"一共猜了{i}次")
        break
# print(f"一共猜了{i}次")
# 4.计算100-999之间的水仙花数
import math
for i in range(100, 1000):
    if math.pow((i%10),3)+math.pow((i//10%10),3)+math.pow((i//100),3)==i:
        print(i)

"""实操案例6"""
# 1.千年危机（千年虫问题）
year=[82,89,88,86,85,00,99]
print(year)
for index,value in enumerate(year):    # 将列表的索引和值匹配
    print(index,value)
    if str(value)!="0":
        year[index]=int('19'+str(value))
    else:
        year[index]=int('200'+str(value))
print(year)
year.sort()
print(year)
# 2.购物流程
lst=[]
for i in range(0,5):
    goods=input("入库商品：")
    lst.append(goods)
for item in lst:
    print(item)
cart=[]
while True:
    num=input("输入要购买的商品编号：")
    for item in lst:
        if item.find(num)!=-1:
            cart.append(item)
            break
    if num=='q':
        break
print("购物车中的商品：")
for m in cart:
    print(m)
print("----------------")
for i in range(len(cart)-1,-1,-1):
    print(cart[i])
print("----------------")
for i in range(-1,-(len(cart)+1),-1):
    print(cart[i])

"""实操案例7"""
# 1.列表转集合
constellation=["狮子座","双子座"]
nature=["多愁善感","积极乐观"]
a=zip(constellation,nature)
for item in a:
    print(item)
print("---------------------------")
a=dict(zip(constellation,nature))
print(a)
for item in a:
    print(item,a[item])
key=input("请输入星座：")
print(key,"的性格特点为：",a.get(key))
# 2.模拟订购火车票
d={"A":["1","a","1a"],"B":["2","b","2b"]}
for item in d:
    print(item,end="   ")
    for i in d[item]:
        print(i, end="   ")
    print()
p=input("输入购票：")
print(f"车次：{p}的信息为    {d[p][0]}    {d[p][1]}    {d[p][2]}")

"""实操案例8"""
# 1.元组做咖啡
coffee_name = ("蓝山", "拿铁", "卡布奇诺")
print("可选咖啡有：")
for index, item in enumerate(coffee_name):
    print(index + 1, '.', item)
i = int(input("请选择：")) - 1
if 0 <= i < len(coffee_name):
    print(f"您的咖啡[{coffee_name[i]}]")
else:
    print("无该咖啡")
# 2.显示前5名
scores=(("广州", 72), ("北京", 70), ("上海", 66), ("江苏", 53), ("山东", 51),)
for index, item in enumerate(scores):
    print(index + 1, '.', end = ' ')
    for i in item:
        print(i, end = ' ')
    print()
# 3.模拟手机通信录
phone = set()
for i in range(1, 6):
    info = input(f"输入第{i}个联系人的姓名和手机号：")
    phone.add(info)
for item in phone:
    print(item)

"""实操案例9"""
# 1.字符次数
def get_count(s, ch):
    count = 0
    for item in s:
        if ch.upper() == item or ch.lower() == item:
            count += 1
    return count
s = "qwertyuiopasdfghjklzxcvbnmwertyudfghertyufgrty"
ch = 'h'
print(get_count(s, ch))
# 2.格式化输出
lst = [["01", "dfs", "md", 500],
       ["02", "xyj", "tcl", 1000],
       ["03", "wbl", "lb", 400]]
for it in lst:
    for jt in it:
        print(jt, end = "\t\t")
    print()
print("------------------------------------------------")
for it in lst:
    it[0] = "000" + it[0]
    it[3] = "${:.2f}".format(it[3])
    for jt in it:
        print(jt, end = "\t\t")
    print()

"""实操案例10"""
# 1.mini计算机
def add(a, b):
    return a + b
def calc(a, b, op):
    if op == "+":
        return add(a, b)
a = int(input("a = "))
b = int(input("b = "))
op = input("op = ")
print(calc(a, b, op))
# 2.猜数
import random
def guess(num, guess_num):
    if num < guess_num:
        return -1
    elif num > guess_num:
        return 1
    else:
        return 0
guess_num = random.randint(1, 100)
while True:
    num = int(input("请猜："))
    r = guess(num, guess_num)
    if r == -1:
        print("小了")
    elif r == 1:
        print("大了")
    else:
        print("猜对了")
        break

"""实操案例11"""
# 1.异常处理
score = int(input("请输入分数："))
if 0 <= score <=100:
    print("分数为：", score)
else:
    raise Exception("分数不正确")    # 手动抛异常，这里异常会由Python解释器捕获
print("-----------------------")
try:
    score = int(input("请输入分数："))
    if 0 <= score <=100:
        print("分数为：", score)
    else:
        raise Exception("分数不正确")    # 手动抛异常，这里异常会由except捕获
except Exception as e:
    print(e)
# 2.三角形判断
def is_triangle(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise Exception("三边不可为负数")
    if a + b > c and b + c > a and a + c > b:
        print(f"三角形三边长为：a = {a}, b = {b}, c = {c}")
    else:
        raise Exception("不构成三角形")
try:
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    is_triangle(a, b, c)
except ValueError as a:
    print(a)
except Exception as e:
    print(e)

"""实操案例12"""
# 1.圆类计算面积和周长
import math
class Circle():
    def __init__(self, r):
        self.r = r
    def get_area(self):
        return math.pi*math.pow(self.r, 2)
    def get_perimeter(self):
        return math.pi * 2 * self.r
C = Circle(1)
print(C.get_area())
print(C.get_perimeter())
# 2.信息列表存储
class Student():
    def __init__(self, name, age, gender, score):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score
    def show(self):
        print(self.name, self.age, self.gender, self.score)
lst = []
for i in range(1, 4):
    s = input(f"请输入第{i}位学生的信息：")
    s_lst = s.split("#")
    stu = Student(s_lst[0], s_lst[1], s_lst[2], s_lst[3])
    lst.append(stu)
for it in lst:
    it.show()

"""实操案例12"""
# 1.多态乐器
class Instrument():
    def make_sound(self):
        pass
class Erhu(Instrument):
    def make_sound(self):
        print("二胡在演奏")
class Pinao(Instrument):
    def make_sound(self):
        print("钢琴在演奏")
class Violin(Instrument):
    def make_sound(self):
        print("小提琴在演奏")
def play(instrument):
    instrument.make_sound()
play(Erhu())
play(Pinao())
play(Violin())
print("---------------")
Erhu().make_sound()
Pinao().make_sound()
Violin().make_sound()
class Bird():
    def make_sound(self):
        print("小鸟在唱歌")
play(Bird())
Bird().make_sound()
# Python的多态更加宽容，只要像鸭子它就是鸭子
# 2.自定义类汽车
class Car():
    def __init__(self, type, no):
        self.type = type
        self.no = no
    def start(self):
        pass
    def stop(self):
        pass
class Taxi(Car):
    def __init__(self, type, no, company):
        super().__init__(type, no)
        self.company = company
    def start(self):
        print(f"出租车车型：{self.type}, 公司：{self.company}，车牌：{self.no}")
    def stop(self):
        print("出租车到达目的地")
class FamilyCar(Car):
    def __init__(self, type, no, name):
        super().__init__(type, no)
        self.name = name
    def start(self):
        print(f"我是：{self.name}，我的汽车我做主")
        print(f"我的车型：{self.type}，我的车牌：{self.no}")
    def stop(self):
        print("我的车到达目的地")
taxi = Taxi("大众", "123434A", "长城公司")
taxi.start()
taxi.stop()
family = FamilyCar("丰田", "63454A", "武松")
family.start()
family.stop()

"""实操案例14"""
# 1.漂亮表格模块
import prettytable as pt
def show_ticket(row_num):
    tb = pt.PrettyTable()
    tb.field_names = ["行号", "座位1", "座位2", "座位3", "座位4", "座位5"]
    for i in range(row_num):
        lst = [f"第{i + 1}行", "有票", "有票", "有票", "有票", "有票" ]
        tb.add_row(lst)
    print(tb)
show_ticket(13)
def order_ticket(row_num, row, column):
    tb = pt.PrettyTable()
    tb.field_names = ["行号", "座位1", "座位2", "座位3", "座位4", "座位5"]
    for i in range(row_num):
        lst = [f"第{i + 1}行", "有票", "有票", "有票", "有票", "有票"]
        if int(row) == i + 1:
            lst[int(column)] = "已售"
        tb.add_row(lst)
    print(tb)
order_ticket(13, 5, 2)
# 2.推算几天后的日期
import datetime
def input_date():
    indate = input("输入日期（如：20201116）：")
    indate = indate.strip()    # 去掉空格
    datestr = indate[0:4] + '-' + indate[4:6] + '-' + indate[6:]
    print(datestr, type(datestr))
    return datetime.datetime.strptime(datestr, "%Y-%m-%d")    # 字符串转日期时间
sdate = input_date()
print(sdate, type(sdate))
in_num = int(input("请输入间隔天数："))
fdate = sdate + datetime.timedelta(days = in_num)    # 这里的 + 一定被重载了
print("推算的日期是：", fdate)
print("推算的日期是："+str(fdate).split(' ')[0])

"""实操案例15"""
# 1.记录用户登录日志
import time
print(time.time())    # 秒
print(time.localtime(time.time()))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
def write_logininfo(username):
    with open("log.txt", 'a', encoding='utf-8') as file:
        s = f'用户名：{username}， 登录时间：{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))}'
        file.write(s)
        file.write("\n")
def read_logininfo():
    print("查看登录日志")
    with open("log.txt", 'r', encoding='utf-8') as file:
        # line = file.readlines()
        # print(line)
        while True:
            line = file.readline()
            if line == '':
                break
            else:
                print(line, end='')
username = input("用户名：")
pwd = input("密码：")
if "admin" == username and "123" == pwd:
    print("成功")
    write_logininfo(username)
    c = input("输入提示数字（0.退出，1.查看登录日志），执行操作：")
    while True:
        if c == '0':
            print("退出")
            break
        elif c == '1':
            read_logininfo()
            c = input("输入提示数字（0.退出，1.查看登录日志），执行操作：")
        else:
            print("输入有误")
else:
    print("用户名或密码错误")
# 2.机器人客服
def find_answer(question):
    with open("replay.txt", 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            keyword = line.split(' ')[0]
            replayword = line.split(' ')[1]
            if keyword in question:
                return replayword
question = input("问题：")
print(find_answer(question))
