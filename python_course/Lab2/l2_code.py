def esc(code):
    return f'\u001b[{code}m'


def flag_bg():
    print(GREEN + ' ' * 24 + END)
    for i in range(3):
        print(GREEN + ' ' * (8 - i) + RED + ' ' * (2 * i + 4) + GREEN + ' ' * (12 - i) + END)

    for i in range(3):
        print(GREEN + ' ' * (6 + i) + RED + ' ' * (8 - 2 * i) + GREEN + ' ' * (10 + i) + END)

    print(GREEN + ' ' * 24 + END)

def pattern(): 
    print(BLACK + ' ' * 5 + WHITE + '  ' + END)
    print(BLACK + ' ' + WHITE + '   ' + BLACK + ' ' + WHITE + '  ' + END)
    print(BLACK + ' ' + WHITE + ' ' + BLACK + '   ' + WHITE + '  ' + END)
    print(BLACK + ' ' + WHITE + ' ' + BLACK + ' ' + WHITE + '    ' + END)
    print(BLACK + ' ' + WHITE + ' ' + BLACK + '     ' + END)

def array_init(array_in, st):
    for i in range(10):
        for j in range(10):
            if j == 0:
                array_in[i][j] = round(st * (8 - i) + st, 1)
            if i == 9:
                array_in[i][j] = round(j, 1)
    return array_in


def array_fill(array_fi, res, st):
    for i in range(9):
        for k in range(10):
            if abs(array_fi[i][0] - res[9 - k]) < st:
                for j in range(9):
                    if 8 - j == k:
                        array_fi[i][j + 1] = 1
    return array_fi


def print_plot(plot):
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += WHITE + str(plot[i][j])
            if plot[i][j] == 0:
                line += '  '
            elif plot[i][j] == 1:
                line += RED + '  ' + WHITE
        line += END
        print(line)
    print(WHITE + '0   1 2 3 4 5 6 7 8 9' + END)


RED = esc(41)
GREEN = esc(42)
BLUE = esc(44)
WHITE = esc(47)
BLACK = esc(40)
END = esc(0)

array_plot = [[0 for col in range(10)] for row in range(10)]
result = [0 for i in range(10)]

print('flag')
flag_bg()
print('pattern')
pattern()
print('y=2x+3')

for i in range(10):
    result[i] = 2 * i + 3

step = round(abs((result[9] - result[0])) / 9, 1)

array_init(array_plot, step)
array_fill(array_plot, result, step)
print_plot(array_plot)

print('Книги до 2015 года и после')
import csv
with open('books.csv', 'r', encoding='windows-1251') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    c15 = 0
    c = 0
    for row in list(table)[1:]:
        if int((row[6])[0:4]) >= 2015:
            c15 += 1
        else:
            c += 1
    all = c + c15
    p1 = round(c / all, 2) * 100
    p2 = round(c15 / all, 2) * 100
    print(p1, '%', RED + ' ' * int(p1) + END)
    print(p2, '%', BLUE + ' ' * int(p2) + END)

