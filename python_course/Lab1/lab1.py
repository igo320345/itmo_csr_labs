import csv

with open('books.csv', 'r', encoding='windows-1251') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    result = open('result.txt', 'w')
    c0 = 0
    c30 = 0
    author = input('Имя автора: ')
    books = []
    links = []
    print(author)
    i = int(input('Номер записи для создания 20 библиографических ссылок: '))
    for idx, row in enumerate(list(table)[1:]):
        if i <= idx <= i + 20:
            link = row[3] + '. ' + row[1] + ' - ' + row[6]
            result.write(link)
            result.write('\n')
        if len(row[1]) > 30:
            c30 += 1
        if row[3] == author or row[4] == author:
            books.append(row)
        c0 += 1
    print('Количество записей:', c0)
    print('Количество записей, у которых в поле Название строка длиннее 30 символов:', c30)
    print('Книги автора ', author, ': ', books )
    print('20 библиографических ссылок записано в файл result.txt')
