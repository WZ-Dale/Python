# @License : 西安工业大学
# @Author  : 王泽 WZ-Dale
# @Time    : 2020/11/12 19:22

import os

filename = "student.txt"

def menu():
    print("====================学生信息管理系统====================")
    print("----------------------功 能 菜 单----------------------")
    print("0.退出")
    print("1.录入 学生信息")
    print("2.查找 学生信息")
    print("3.删除 学生信息")
    print("4.修改 学生信息")
    print("5.排序 学生信息")
    print("6.统计 学生人数")
    print("7.显示 学生信息")
    print("------------------------------------------------------")

def main():
    while True:
        menu()
        choice = int(input("请选择："))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice == 0:
                answer = input("您确认退出系统吗？（y/n）：")
                if answer == 'y' or answer == 'Y':
                    print("感谢您的使用！！")
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()

def insert():
    student_list = []
    while True:
        id = input("请输入ID（如：1001）：")
        if not id:
            break
        name = input("请输入姓名：")
        if not name:
            break
        try:
            Chinese = int(input("请输入语文成绩："))
            Math = int(input("请输入数学成绩："))
            English = int(input("请输入英语成绩："))
        except:
            print("输入无效，不是整数类型，请重新输入：")
            continue
        # 将学生信息添加到字典中
        student = {"id":id,"name":name,"Chinese":Chinese,"Math":Math,"English":English}
        # 将学生信息添加到列表中
        student_list.append(student)
        answer = input("是否继续录入？（y/n）：")
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
    # 调用save()函数，将信息保存到文件中
    save(student_list)
    print("学生信息录入完毕！！")

def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()

def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input("请输入查询依据（1.ID/2.姓名）：")
            if mode == '1':
                id = input("请输入学生ID：")
            elif mode == '2':
                name = input("请输入学生姓名：")
            else:
                print("输入有误，请重新输入：")
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:
                student_list = rfile.readlines()
            for item in student_list:
                d = dict(eval(item))
                if mode == '1' and d['id'] == id:
                    student_query.append(d)
                elif mode == '2' and d['name'] == name:
                    student_query.append(d)
            show_student(student_query)
            student_query.clear()
            answer = input("是否继续查询（y/n）：")
            if answer == 'y' or answer == 'Y':
                continue
            else:
                return
        else:
            print("暂未保存学生信息")
            return

def show_student(lst):
    if len(lst) == 0:
        print("没查到学生信息，无数据显示！！")
        return
    else:
        format_title = "{:^6}\t{:^12}\t{:^10}\t{:^10}\t{:^10}\t{:^10}"
        print(format_title.format('ID','姓名','语文成绩','数学成绩','英语成绩','总成绩'))
        format_data = "{:^6}\t{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}"
        for item in lst:
            print(format_data.format(item['id'],item['name'],item['Chinese'],item['Math'],item['English'],
                                     int(item['Chinese'])+int(item['Math'])+int(item['English'])))

def delete():
    while True:
        student_id = input("请输入要删除的学生ID：")
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False    # 标记是否删除了
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))    # 将字符串转为字典
                        if d['id'] != student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag = True
                    if flag:
                        print(f"ID为{student_id}的学生信息已被删除")
                    else:
                        print(f"未找到ID为{student_id}的学生信息")
            else:
                print("文件内无学生信息")
                break
            show()    # 显示删除后的所有学生信息
            answer = input("是否继续删除学生信息（y/n）：")
            if answer == 'y':
                continue
            else:
                break

def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input("请输入要修改的学生ID：")
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print("已找到该学生信息，可以进行修改操作！！")
                while True:
                    try:
                        d['name'] = input("请输入姓名：")
                        d['Chinese'] = input("请输入语文成绩：")
                        d['Math'] = input("请输入数学成绩：")
                        d['English'] = input("请输入英语成绩：")
                    except:
                        print("输入无效，请重新输入：")
                        continue
                    else:
                        break
                wfile.write(str(d)+'\n')
                print("修改成功！！")
            else:
                wfile.write(str(d)+'\n')
        answer = input("是否继续修改其它学生信息（y/n）：")
        if answer == 'y' or answer == 'Y':
            modify()
        else:
            return

def sort():
    show()
    student_lst = []
    flag = True
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list = rfile.readlines()
        for item in student_list:
            d = dict(eval(item))
            student_lst.append(d)
        mode = input("请选择排序方式（0.升序/1.降序）：")
        if mode == '0':
            flag = False
        elif mode == '1':
            flag = True
        else:
            print("选择有误！请重新选择：")
            sort()
        answer = input("请选择排序依据（1.语文/2.数学/3.英语/4.总成绩）：")
        if answer == '1':
            student_lst.sort(key=lambda x : int(x['Chinese']),reverse=flag)
        elif answer == '2':
            student_lst.sort(key=lambda x : int(x['Math']),reverse=flag)
        elif answer == '3':
            student_lst.sort(key=lambda x : int(x['English']),reverse=flag)
        elif answer == '4':
            student_lst.sort(key=lambda x: int(x['Chinese'])+int(x['Math'])+int(x['English']), reverse=flag)
        else:
            print("选择有误！请重新选择：")
            sort()
        show_student(student_lst)
    else:
        print("暂未保存数据信息！！")

def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list = rfile.readlines()
        if student_list:
            print(f"一共有{len(student_list)}名学生")
        else:
            print("未录入学生信息！！")
    else:
        print("暂未保存数据信息！！")

def show():
    student_lst = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list = rfile.readlines()
        for item in student_list:
            d = dict(eval(item))
            student_lst.append(d)
        if student_lst:
            show_student(student_lst)
    else:
        print("暂未保存数据信息！！")

if __name__ == '__main__':
    main()