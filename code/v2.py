import sys

# 获取宝可梦的名称
poke_name = sys.argv[1]

# 读取poke.txt文件
file = open('poke.txt', 'r', encoding='utf-8')
content = file.read()
file.close()

# 把正确的内容存到poke_dict
poke_dict = {}
line_list = content.split('\n')
for line in line_list:
    field_list = line.split('\t')
    if len(field_list) == 4:
        key = field_list[1]
        url = 'https://wiki.52poke.com/wiki/' + key
        poke_dict[key] = url + ' ' + line

# 查找输入的宝可梦是否存在于poke_dict
value = poke_dict[poke_name]
print(poke_name + ': ' + value)