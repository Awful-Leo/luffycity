# -*- coding:utf-8 -*-
menu = [{
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车站': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}]
while True:
    if len(menu) == 0:
        exit()
    for item in menu[-1]:
        print(item)
    s = input('>>>')
    if s == 'q':
        exit('再见')
    elif s in menu[-1]:
        menu.append(menu[-1][s])
    elif s == 'b':
        menu.pop()
    else:
        print('Sorry, invalid input. Please try again')
