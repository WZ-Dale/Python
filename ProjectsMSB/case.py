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

