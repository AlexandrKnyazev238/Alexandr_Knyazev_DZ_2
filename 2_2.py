# Task_2

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
for elem in my_list:
    if elem.isdigit():
        new_list.extend(['"', f'{int(elem):02}', '"'])
    elif (elem.startswith('+') or elem.startswith('-')) and elem[1:].isdigit():
        new_list.extend(['"', f'{elem[0]}{int(elem[1:]):02}', '"'])
    else:
        new_list.append(elem)
out_list = ' '.join(new_list)
print(out_list)

symbol_idxs = []
for idx, letter in enumerate(out_list):
    if letter == '"':
        symbol_idxs.append(idx)
for idx in range(len(symbol_idxs)):
    if idx % 2 == 0:
        symbol_idxs[idx] = symbol_idxs[idx] + 1
    else:
        symbol_idxs[idx] = symbol_idxs[idx] - 1
for del_idx in reversed(symbol_idxs):
    out_list = out_list[:del_idx] + out_list[del_idx+1:]
