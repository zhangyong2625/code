"""
  @Author : zhangyong2625
  @Email : 1293271923@qq.com
"""
"""
使用python开发一个猜数小游戏.在游戏中，程序每一轮会随机生成一个0-1024之间的数字，用户输入猜测的数字，程序告诉用户猜大了还是猜小了。在一定次数内猜对，则本轮用户获胜，否则本轮用户失败。
每一轮开始时，程序会要求用户输入用户名。
程序会一直运行下去，知道用户输入数字“3”，停止游戏。在每一轮开始前，输入“1”可以查看用户的输入历史。
"""
import random
import sys

# 输入数字"1"查看历史记录    
def history(dict_hisory):
    for key,value in dict_hisory.items():
        print("用户名：%s，记录如下：%s"%(key,value))

# 输入数字"2"猜数游戏
def guess(number,flag):
    # print("正确答案：%s"%number)
    while(flag>0):
        guess_number = int(input("请输入一个数字："))
        if guess_number>number:
            print("你输入的数字比正确答案大")
        elif guess_number<number:
            print("你输入的数字比正确答案小")
        else:
            print("恭喜！猜对了")
            return "成功"
        guess(number,flag-1)
        return "失败"
    print("猜错次数太多，失败。")
    # return "失败" # ！！！return语句不能放在此处，否则会死循环(放第27行)

# 输入数字"3"退出游戏
def exit_guess():
    sys.exit()

# 打印每一轮的提示文案
def tips(count):
    print("-"*20+"第%s轮游戏"%count+"-"*20)
    tip = "1.历史记录\n2.继续游戏\n3.退出游戏" 
    print(tip)

# 游戏开始
def run():
    count = 1 #记录目前是第几轮
    flag = 10 #控制每轮猜的次数
    dict_hisory = {}
    while(1):
        tips(count)
        num = int(input("请输入数字选择："))
        if num==1:
            history(dict_hisory)
            continue
        elif num==2:
            name = input("请输入您的名字：")
            number = random.randint(0,1024)
            result = guess(number,flag)
            if name in dict_hisory.keys():
                dict_hisory[name].append(result)
            else:
                dict_hisory[name] = [result]
        elif num==3:
            exit_guess()
        else:
            print("输入有误！")
            continue
        count += 1

if __name__ == "__main__":
    run()
        
        
        