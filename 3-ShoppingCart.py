# -*- coding:utf-8 -*-
import random
import getpass

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]

# 用户登录


def login():
    print('请登录!')
    userName = input('账号: ').strip()
    passWord = getpass.getpass('密码: ')
    print('登录成功!')
    shoppingCart()

# 购物


def shoppingCart():
    while True:
        balance = input('请输入您的工资: ').strip()
        if not balance.isdigit():
            print('输入无效!')
        else:
            balance = int(balance)
            break
    purchased_goods = {}
    while True:
        # 打印商品列表
        global goods
        for number, good in enumerate(goods):
            print(number, good['name'], ':', good['price'])
        choice = input('请输入编号以购买商品:(按Q退出,按C查看余额)').strip()
        # 按q退出
        if choice.lower() == 'q':
            # 打印已购买商品
            if len(purchased_goods) == 0:
                print('您没有购买任何商品。')
            else:
                print('您一共购买了如下商品:')
                for name, quantity in purchased_goods.items():
                    print(
                        '\033[31m%s\033[0m个\033[31m%s\033[0m' %
                        (quantity, name))
            # 退出程序
            exit('欢迎下次光临，再见!')
        # 按c查询余额
        if choice.lower() == 'c':
            print('您的当前余额为\033[31m%s\033[0m' % balance)
            continue
        # 检测无效数字
        if not choice.isdigit():
            print('输入无效，请重新输入整数数字')
        else:
            choice = int(choice)
            #数字编号合法
            if choice < len(goods):
                #余额不足，提示无法购买
                if balance < goods[choice]['price']:
                    print(
                        '\033[31;1m当前余额为%s\033[0m，无法选购此物品，请重新选购!\033[0m' %
                        balance)
                else:
                    balance -= goods[choice]['price']
                    purchased_goods[goods[choice]['name']] = purchased_goods.get(
                        goods[choice]['name'], 0) + 1
                    print('您已成功购买%s' % goods[choice]['name'])
            #数字超出范围，提示不存在
            else:
                print('抱歉，此商品不存在，请重新输入!')


if __name__ == '__main__':
    login()
