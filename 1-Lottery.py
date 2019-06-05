# -*- coding:utf-8 -*-

def lottery():
    print('Welcome to Leo\'s lottery station')
    redballs, blueballs = [], []
    colors = [('red', '\033[31m', 6, 32), ('blue', '\033[34m', 2, 16)]
    string = '%s[%s] select %s ball:'
    for color in colors:
        for i in range(1, color[2] + 1):
            input_valid = False
            while not input_valid:
                ball = input(string % (color[1], i, color[0])).strip()
                if not ball.isdigit():
                    print('Please input numbers only')
                else:
                    ball = int(ball)
                    if ball not in range(1, color[3] + 1):
                        print('Please only select numbers between 1 and %s' % color[3])
                    elif ball in eval('%sballs' % color[0]):
                        print(
                            'Sorry, number %d already exists in %s ball list' %
                            (ball, color[0]))
                    else:
                        input_valid = True
                        exec('%sballs.append(ball)' % color[0])
    print('\n' * 2)
    print(colors[0][1] + 'Red balls: %s' % redballs)
    print(colors[1][1] + 'Blue balls: %s' % blueballs)
    print('Good luck!')


if __name__ == '__main__':
    lottery()
