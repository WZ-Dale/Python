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



