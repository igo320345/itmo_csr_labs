def bag_items(items, bag_size):
    item_size = [items[item][0] for item in items]
    item_xp = [items[item][1] for item in items]
    n = len(items) 
    table = [[0 for a in range(bag_size+1)] for i in range(n+1)]
    for i in range(n + 1):
        for j in range(bag_size + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif item_size[i - 1] <= j:
                table[i][j] = max(item_xp[i - 1] + table[i - 1][j - item_size[i - 1]], table[i-1][j])
            else:
                table[i][j] = table[i - 1][j]

    max_xp = table[n][bag_size]      
    max_size = bag_size              
    items_list = []    
    for i in range(n, 0, -1):  
        if max_xp <= 0: 
            break
        if max_xp == table[i - 1][max_size]:  
            continue
        else:
            items_list.append((item_size[i - 1], item_xp[i - 1]))
            max_xp -= item_xp[i - 1]   
            max_size -= item_size[i - 1]

    items_keys = []
    xp = 0
    for item in items_list:
        for k, v in items.items():
            if v == item:
                items_keys.append((k, v[0]))
                items.pop(k)
                xp += v[1]
                break
    return ''.join([i[0] * i[1] for i in items_keys]), xp


items = {'в': (3, 25),
         'п': (2, 15),
         'б': (2, 15),
         'а': (2, 20),
         'и': (1, 5),
         'н': (1, 15),
         'т': (3, 20),
         'о': (1, 25),
         'ф': (1, 15),
         'д': (1, 10),
         'к': (2, 20),
         'р': (2, 20)
        }


bag_size = 3 * 3
items.pop('и')
bag, xp = bag_items(items, bag_size - 1)
bag += 'и'
print('Итоговые очки выживания: ', xp - sum([items[item][1] for item in  items]))
for i in range(bag_size):
    print(bag[i], end=' ')
    if (i + 1) % 3 == 0:
        print()
